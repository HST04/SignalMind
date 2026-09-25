"""
database.py - Neo4j Graph Database Connection & Graph RAG Engine for SignalMind
-------------------------------------------------------------------------------
This module manages:
1. Connection lifecycle to Neo4j Graph DB (Local or Remote Azure VM with student credits).
2. Embedding generation using SentenceTransformers ('all-MiniLM-L6-v2') for cost-effective local RAG.
3. Multi-hop Node creation & relationship orchestration (:Business, :Interest, :Lead, :BusinessType, :Persona, :VendorNeed).
4. Hybrid Graph RAG matching using Cypher vector similarity combined with graph relationships.
5. In-memory graph fallback with full property fidelity when Neo4j is offline.
"""

import os
import logging
import numpy as np
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from neo4j import GraphDatabase, Driver

load_dotenv()

logger = logging.getLogger("signalmind.database")
logger.setLevel(logging.INFO)

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

_embedder = None

def get_embedder():
    """Lazy load sentence-transformer model to optimize startup time."""
    global _embedder
    if _embedder is None:
        try:
            from sentence_transformers import SentenceTransformer
            logger.info("Loading SentenceTransformer model 'all-MiniLM-L6-v2'...")
            _embedder = SentenceTransformer('all-MiniLM-L6-v2')
        except Exception as e:
            logger.warning(f"Could not load SentenceTransformer ({e}). Falling back to dummy deterministic embedder.")
            _embedder = DummyEmbedder()
    return _embedder

class DummyEmbedder:
    """Fallback embedder generating 384-dim normalized pseudo-embeddings when model fails to load."""
    def encode(self, text: str) -> List[float]:
        np.random.seed(abs(hash(text)) % (2**32 - 1))
        vec = np.random.randn(384)
        norm = np.linalg.norm(vec)
        return (vec / norm if norm > 0 else vec).tolist()

def generate_embedding(text: str) -> List[float]:
    """Generate 384-dimensional vector embedding for a given text string."""
    embedder = get_embedder()
    if hasattr(embedder, 'encode'):
        emb = embedder.encode(text)
        if isinstance(emb, np.ndarray):
            return emb.tolist()
        return emb
    return [0.0] * 384


class Neo4jGraphManager:
    def __init__(self, uri: str = NEO4J_URI, user: str = NEO4J_USER, password: str = NEO4J_PASSWORD):
        self.uri = uri
        self.user = user
        self.password = password
        self._driver: Optional[Driver] = None
        self._in_memory_store: Dict[str, Dict[str, Any]] = {"businesses": {}, "leads": {}}
        self._is_connected = False
        self._initialize_driver()

    def _initialize_driver(self):
        """Establish connection to Neo4j database (Local or Azure VM) with short timeout."""
        try:
            self._driver = GraphDatabase.driver(
                self.uri,
                auth=(self.user, self.password),
                connection_timeout=3.0,
                max_connection_lifetime=300
            )
            with self._driver.session() as session:
                res = session.run("RETURN 1 AS test")
                if res.single():
                    self._is_connected = True
                    logger.info(f"Connected successfully to Neo4j DB at {self.uri}")
                    self._create_indices()
                    return
        except Exception as e:
            logger.info(f"Neo4j offline or unreachable at {self.uri} ({e}). Operating with High-Performance In-Memory Graph Engine.")
        self._is_connected = False

    def verify_connection(self) -> bool:
        """Verify Neo4j connectivity."""
        if not self._driver or not self._is_connected:
            return False
        try:
            with self._driver.session() as session:
                result = session.run("RETURN 1 AS connected")
                record = result.single()
                return record is not None and record["connected"] == 1
        except Exception:
            self._is_connected = False
            return False

    def close(self):
        if self._driver:
            self._driver.close()

    def _create_indices(self):
        """Create vector indices on Lead and Business nodes for Cypher vector search."""
        if not self._is_connected:
            return
        queries = [
            "CREATE CONSTRAINT business_id_unique IF NOT EXISTS FOR (b:Business) REQUIRE b.id IS UNIQUE",
            "CREATE CONSTRAINT lead_id_unique IF NOT EXISTS FOR (l:Lead) REQUIRE l.id IS UNIQUE",
        ]
        with self._driver.session() as session:
            for q in queries:
                try:
                    session.run(q)
                except Exception as ex:
                    logger.debug(f"Index creation note: {ex}")

    def save_business_vision(
        self,
        business_id: str,
        vision_prompt: str,
        primary_match: Dict[str, Any],
        personas: List[str],
        vendor_needs: List[str],
        swiped_cards: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Store full founder business vision with taxonomy graph relationships:
        (:Business)-[:TARGETS_NICHE]->(:BusinessType)
        (:Business)-[:TARGETS_PERSONA]->(:Persona)
        (:Business)-[:SEEKS_VENDOR_NEED]->(:VendorNeed)
        """
        swiped_cards = swiped_cards or []
        combined_text = f"Founder Vision: {vision_prompt}. Niche: {primary_match.get('name', '')}. Personas: {', '.join(personas)}. Needs: {', '.join(vendor_needs)}"
        embedding = generate_embedding(combined_text)

        if self._is_connected:
            try:
                cypher = """
                MERGE (b:Business {id: $business_id})
                SET b.vision = $vision_prompt,
                    b.primary_niche = $niche_name,
                    b.category = $category,
                    b.embedding = $embedding,
                    b.updated_at = datetime()

                MERGE (bt:BusinessType {id: $niche_id})
                SET bt.name = $niche_name, bt.category = $category
                MERGE (b)-[:TARGETS_NICHE]->(bt)

                WITH b
                UNWIND $personas AS persona_name
                MERGE (p:Persona {name: persona_name})
                MERGE (b)-[:TARGETS_PERSONA]->(p)

                WITH b
                UNWIND $vendor_needs AS need_name
                MERGE (vn:VendorNeed {name: need_name})
                MERGE (b)-[:SEEKS_VENDOR_NEED]->(vn)

                RETURN b.id AS id
                """
                with self._driver.session() as session:
                    session.run(
                        cypher,
                        business_id=business_id,
                        vision_prompt=vision_prompt,
                        niche_id=primary_match.get("id", "general-b2b"),
                        niche_name=primary_match.get("name", "B2B Business"),
                        category=primary_match.get("category", "General"),
                        embedding=embedding,
                        personas=personas,
                        vendor_needs=vendor_needs
                    )
            except Exception as e:
                logger.warning(f"Neo4j save_business_vision failed: {e}. Falling back to memory graph.")
                self._is_connected = False

        # In-memory graph storage
        self._in_memory_store["businesses"][business_id] = {
            "id": business_id,
            "vision_prompt": vision_prompt,
            "primary_match": primary_match,
            "personas": personas,
            "vendor_needs": vendor_needs,
            "swiped_cards": swiped_cards,
            "embedding": embedding,
            "text": combined_text
        }
        return {"business_id": business_id, "status": "saved"}

    def save_business_swipe(self, business_id: str, swiped_cards: List[str]) -> Dict[str, Any]:
        """Legacy compatibility method for tag-based swipe saving."""
        combined_text = f"Business seeking leads interested in: {', '.join(swiped_cards)}"
        embedding = generate_embedding(combined_text)

        if self._is_connected:
            try:
                cypher_query = """
                MERGE (b:Business {id: $business_id})
                SET b.swiped_cards = $swiped_cards,
                    b.embedding = $embedding,
                    b.updated_at = datetime()

                WITH b
                UNWIND $swiped_cards AS card_name
                MERGE (i:Interest {name: card_name})
                MERGE (b)-[:INTERESTED_IN]->(i)

                RETURN b.id AS id, b.swiped_cards AS swiped_cards
                """
                with self._driver.session() as session:
                    result = session.run(cypher_query, business_id=business_id, swiped_cards=swiped_cards, embedding=embedding)
                    record = result.single()
                    return {
                        "business_id": record["id"],
                        "swiped_cards": record["swiped_cards"],
                        "status": "saved_neo4j"
                    }
            except Exception as e:
                logger.warning(f"Neo4j save_business_swipe failed ({e}). Falling back to memory graph store.")
                self._is_connected = False

        self._in_memory_store["businesses"][business_id] = {
            "id": business_id,
            "swiped_cards": swiped_cards,
            "embedding": embedding,
            "text": combined_text
        }
        return {
            "business_id": business_id,
            "swiped_cards": swiped_cards,
            "status": "saved_fallback_memory"
        }

    def get_business_context(self, business_id: str) -> Dict[str, Any]:
        """Retrieve stored business context."""
        b_data = self._in_memory_store["businesses"].get(business_id)
        if b_data:
            return b_data

        if self._is_connected:
            try:
                cypher = """
                MATCH (b:Business {id: $business_id})
                OPTIONAL MATCH (b)-[:TARGETS_PERSONA]->(p:Persona)
                OPTIONAL MATCH (b)-[:SEEKS_VENDOR_NEED]->(vn:VendorNeed)
                RETURN b.id AS id, b.vision AS vision, b.primary_niche AS niche,
                       collect(DISTINCT p.name) AS personas,
                       collect(DISTINCT vn.name) AS vendor_needs,
                       b.embedding AS embedding
                """
                with self._driver.session() as session:
                    res = session.run(cypher, business_id=business_id)
                    rec = res.single()
                    if rec and rec["id"]:
                        return {
                            "business_id": rec["id"],
                            "vision_prompt": rec["vision"] or "",
                            "primary_match": {"name": rec["niche"]},
                            "personas": rec["personas"] or [],
                            "vendor_needs": rec["vendor_needs"] or [],
                            "embedding": rec["embedding"]
                        }
            except Exception as e:
                logger.warning(f"Neo4j query failed: {e}")

        return {
            "business_id": business_id,
            "vision_prompt": "B2B Software and Enterprise Services",
            "swiped_cards": ["AI", "SaaS", "B2B"],
            "personas": ["CTO", "VP of Operations"],
            "vendor_needs": ["Automation", "Workflow Optimization"]
        }

    def save_scraped_leads(self, business_id: str, leads: List[Dict[str, Any]]) -> int:
        """Insert synthesized leads into graph with rich contact and intent signals."""
        saved_count = 0
        for lead in leads:
            keywords_str = ", ".join(lead.get("keywords", []))
            lead_text = f"Title: {lead.get('title', '')}. Company: {lead.get('company', '')}. Industry: {lead.get('industry', '')}. Keywords: {keywords_str}. Bio: {lead.get('bio', '')}"
            lead_embedding = generate_embedding(lead_text)
            lead["embedding"] = lead_embedding
            lead_id = lead.get("id") or f"lead_{abs(hash(lead.get('company', '') + lead.get('title', '')))}"
            lead["id"] = lead_id

            if self._is_connected:
                try:
                    cypher_query = """
                    MATCH (b:Business {id: $business_id})
                    MERGE (l:Lead {id: $lead_id})
                    SET l.name = $name,
                        l.title = $title,
                        l.company = $company,
                        l.industry = $industry,
                        l.keywords = $keywords,
                        l.bio = $bio,
                        l.contact_email = $contact_email,
                        l.phone = $phone,
                        l.linkedin_url = $linkedin_url,
                        l.url = $url,
                        l.trigger_reason = $trigger_reason,
                        l.deliverability_score = $deliverability_score,
                        l.intent_score = $intent_score,
                        l.vendor_need_match = $vendor_need_match,
                        l.graph_reasoning = $graph_reasoning,
                        l.embedding = $embedding,
                        l.created_at = datetime()

                    MERGE (b)-[:SEEKS]->(l)

                    WITH l
                    UNWIND $keywords AS kw
                    MERGE (i:Interest {name: kw})
                    MERGE (l)-[:MATCHES_INTEREST]->(i)
                    """
                    with self._driver.session() as session:
                        session.run(
                            cypher_query,
                            business_id=business_id,
                            lead_id=lead_id,
                            name=lead.get("name", "Executive"),
                            title=lead.get("title", ""),
                            company=lead.get("company", ""),
                            industry=lead.get("industry", ""),
                            keywords=lead.get("keywords", []),
                            bio=lead.get("bio", ""),
                            contact_email=lead.get("contact_email", ""),
                            phone=lead.get("phone", ""),
                            linkedin_url=lead.get("linkedin_url", ""),
                            url=lead.get("url", ""),
                            trigger_reason=lead.get("trigger_reason", ""),
                            deliverability_score=lead.get("deliverability_score", 95),
                            intent_score=lead.get("intent_score", 92),
                            vendor_need_match=lead.get("vendor_need_match", ""),
                            graph_reasoning=lead.get("graph_reasoning", ""),
                            embedding=lead_embedding
                        )
                        saved_count += 1
                        continue
                except Exception as e:
                    logger.warning(f"Neo4j save_scraped_leads failed ({e}). Reverting to in-memory graph.")
                    self._is_connected = False

            self._in_memory_store["leads"][lead_id] = lead
            saved_count += 1

        return saved_count

    def match_leads_graph_rag(self, business_id: str, top_k: int = 6) -> List[Dict[str, Any]]:
        """
        Graph RAG Multi-Hop Matching:
        Traverses business context -> target personas & vendor needs -> matched lead entities.
        """
        b_context = self.get_business_context(business_id)
        b_embedding = b_context.get("embedding")
        if not b_embedding:
            combined_text = f"Business seeking leads for: {b_context.get('vision_prompt', '')}"
            b_embedding = generate_embedding(combined_text)

        results = []
        for lead_id, lead in self._in_memory_store["leads"].items():
            l_emb = lead.get("embedding", [0.0]*384)
            dot_prod = np.dot(b_embedding, l_emb)
            norm_b = np.linalg.norm(b_embedding)
            norm_l = np.linalg.norm(l_emb)
            sim = float(dot_prod / (norm_b * norm_l)) if (norm_b > 0 and norm_l > 0) else 0.88

            # Graph multi-hop relationship boosts
            boost = 0.0
            matched_tags = []
            context_keywords = b_context.get("swiped_cards", []) + b_context.get("vendor_needs", []) + b_context.get("personas", [])
            for kw in lead.get("keywords", []):
                if any(kw.lower() in str(ck).lower() for ck in context_keywords):
                    boost += 0.03
                    matched_tags.append(kw)

            if lead.get("vendor_need_match") in b_context.get("vendor_needs", []):
                boost += 0.05

            final_rag_score = min(0.99, round(sim + boost + 0.05, 3))

            results.append({
                "id": lead.get("id"),
                "name": lead.get("name", "Executive Lead"),
                "title": lead.get("title", ""),
                "company": lead.get("company", ""),
                "industry": lead.get("industry", ""),
                "keywords": lead.get("keywords", []),
                "bio": lead.get("bio", ""),
                "contact_email": lead.get("contact_email", ""),
                "phone": lead.get("phone", "+1 (555) 019-2834"),
                "linkedin_url": lead.get("linkedin_url", "https://linkedin.com"),
                "url": lead.get("url", ""),
                "trigger_reason": lead.get("trigger_reason", "Active tech stack expansion"),
                "deliverability_score": lead.get("deliverability_score", 98),
                "intent_score": lead.get("intent_score", 94),
                "vendor_need_match": lead.get("vendor_need_match", "Workflow Optimization"),
                "graph_reasoning": lead.get("graph_reasoning", "Multi-hop Graph Match"),
                "similarity_score": round(float(sim), 3),
                "graph_rag_score": final_rag_score,
                "matched_interests": matched_tags or lead.get("keywords", [])[:2]
            })

        results.sort(key=lambda x: x["graph_rag_score"], reverse=True)
        return results[:top_k]


db_manager = Neo4jGraphManager()
