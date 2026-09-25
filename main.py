"""
main.py - Full-Stack FastAPI Application for SignalMind B2B Lead Intelligence
-----------------------------------------------------------------------------
Serves:
1. Public Landing Page at GET / (Obsidian Liquid Glass Design)
2. Interactive Lead Intelligence Engine Dashboard at GET /app
3. RESTful GraphRAG & AI Decision Pipeline API at /api/*
4. Continuous Dual-Webhook Ingestion Endpoints at /api/webhooks/*
"""

import os
import time
import logging
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from database import db_manager
from agent import generate_lead_profile, generate_outreach_pitch
from scraper import scrape_leads
from taxonomy_engine import taxonomy_engine
import telemetry

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("signalmind.main")

app = FastAPI(
    title="SignalMind B2B Lead Intelligence API",
    description="Full-stack prototype powered by GraphRAG, 200-Business Taxonomy, Groq LLM, and Dual Webhook Telemetry.",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount assets directory if present
if os.path.exists("assets"):
    app.mount("/assets", StaticFiles(directory="assets"), name="assets")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# --- PYDANTIC SCHEMAS ---

class ClassifyRequest(BaseModel):
    vision_prompt: str = Field(..., example="AI automated call dispatching software for roofing and HVAC contractors")

class SynthesizeRequest(BaseModel):
    business_id: Optional[str] = Field("biz_founder_1", description="Unique session or business ID")
    vision_prompt: str = Field(..., description="Founder's description of their solution")
    primary_match: Optional[Dict[str, Any]] = None
    personas: Optional[List[str]] = Field(default_factory=list)
    vendor_needs: Optional[List[str]] = Field(default_factory=list)
    swiped_cards: Optional[List[str]] = Field(default_factory=list)
    use_live_scraper: Optional[bool] = False
    target_url: Optional[str] = ""

class OutreachRequest(BaseModel):
    lead: Dict[str, Any]
    founder_vision: Optional[str] = ""
    vendor_need: Optional[str] = ""

class WebhookSignalRequest(BaseModel):
    source: Optional[str] = "Webhook 1 (Market Ingestion)"
    signal_type: str = Field(..., example="JOB_POSTING")
    company: str = Field(..., example="Titan Skyline Builders")
    details: str = Field(..., example="Posted 3 hiring notices for Dispatch Managers on LinkedIn")
    signal_strength: Optional[str] = "High"

class WebhookEnrichmentRequest(BaseModel):
    company: str = Field(..., example="Veritas Dental Partners")
    details: str = Field(..., example="SMTP mailbox verified, zero bounce risk")
    deliverability: Optional[int] = 98

# Backward compatibility schemas
class SwipeRequest(BaseModel):
    business_id: str
    swiped_cards: List[str]

class SwipeResponse(BaseModel):
    status: str
    message: str
    business_id: str
    swiped_cards: List[str]

class DiscoverRequest(BaseModel):
    business_id: str
    use_live_scraper: Optional[bool] = False
    target_url: Optional[str] = ""


# --- FRONTEND ROUTING ENDPOINTS ---

@app.get("/", response_class=HTMLResponse, tags=["Web Pages"])
def serve_landing_page():
    """Serves the polished SignalMind Landing Page."""
    landing_path = os.path.join(BASE_DIR, "landing.html")
    if not os.path.exists(landing_path):
        landing_path = os.path.join(BASE_DIR, "stitch_landing_page.html")
    with open(landing_path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/app", response_class=HTMLResponse, tags=["Web Pages"])
def serve_app_dashboard():
    """Serves the interactive SignalMind Lead Intelligence Dashboard."""
    app_path = os.path.join(BASE_DIR, "app.html")
    if os.path.exists(app_path):
        with open(app_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h1>SignalMind Lead Engine Loading...</h1>")


# --- TAXONOMY & INTENT CLASSIFICATION API ---

@app.post("/api/taxonomy/classify", tags=["Taxonomy Engine"])
def classify_founder_vision(payload: ClassifyRequest):
    """
    Parses founder natural language vision and maps it against the 200 business taxonomy in data/business_types.json.
    Returns primary match, secondary matches, ideal buyer personas, common vendor needs, ticket size, and sales cycles.
    """
    if not payload.vision_prompt.strip():
        raise HTTPException(status_code=400, detail="Vision prompt cannot be empty.")
    
    result = taxonomy_engine.classify_vision(payload.vision_prompt)
    return result

@app.get("/api/taxonomy/categories", tags=["Taxonomy Engine"])
def get_all_taxonomy_categories():
    """Returns summary breakdown of all 12 industry categories from the 200-item database."""
    return {
        "status": "success",
        "total_business_types": len(taxonomy_engine.business_types),
        "categories": taxonomy_engine.get_all_categories()
    }

@app.get("/api/taxonomy/search", tags=["Taxonomy Engine"])
def search_taxonomy_items(q: str = "", limit: int = 6):
    """Search across 200 curated business types by keyword."""
    return {
        "query": q,
        "results": taxonomy_engine.search_taxonomy(q, limit=limit)
    }


# --- LEAD SYNTHESIS & GRAPHRAG PIPELINE ---

@app.post("/api/leads/synthesize", tags=["Lead Pipeline"])
def synthesize_leads_pipeline(payload: SynthesizeRequest):
    """
    Full 6-Step Lead Synthesis & GraphRAG Pipeline:
    1. Parse Founder Vision & confirmed taxonomy nodes.
    2. Store multi-hop relationships in Neo4j Graph / In-Memory Graph.
    3. Invoke Groq LLM Decision Agent to formulate targeted B2B lead profile.
    4. Synthesize / scrape verified B2B leads.
    5. Ingest into GraphRAG knowledge graph.
    6. Execute multi-hop Graph traversal + vector cosine similarity to return top matched leads.
    """
    start_time = time.time()
    logger.info(f"Executing Lead Synthesis for vision: '{payload.vision_prompt[:60]}...'")

    try:
        # Step 1: Resolve taxonomy if not provided
        primary_match = payload.primary_match
        personas = payload.personas or []
        vendor_needs = payload.vendor_needs or []

        if not primary_match:
            classification = taxonomy_engine.classify_vision(payload.vision_prompt)
            primary_match = classification["primary_match"]
            if not personas:
                personas = classification["aggregated_personas"]
            if not vendor_needs:
                vendor_needs = classification["aggregated_vendor_needs"]

        # Step 2: Save to Graph
        business_id = payload.business_id or f"biz_{abs(hash(payload.vision_prompt)) % 100000}"
        db_manager.save_business_vision(
            business_id=business_id,
            vision_prompt=payload.vision_prompt,
            primary_match=primary_match,
            personas=personas,
            vendor_needs=vendor_needs,
            swiped_cards=payload.swiped_cards
        )

        # Step 3: Groq Decision Agent
        biz_context = {
            "business_id": business_id,
            "vision_prompt": payload.vision_prompt,
            "primary_match": primary_match,
            "personas": personas,
            "vendor_needs": vendor_needs,
            "swiped_cards": payload.swiped_cards or [primary_match.get("name", "B2B")]
        }
        lead_profile = generate_lead_profile(biz_context)

        # Step 4: Web Scraping / Lead Synthesis
        raw_leads = scrape_leads(
            lead_profile=lead_profile,
            use_live=payload.use_live_scraper or False,
            target_url=payload.target_url or ""
        )

        # Step 5: Save leads to Graph
        inserted_count = db_manager.save_scraped_leads(business_id, raw_leads)

        # Step 6: Graph RAG Matching Query
        matched_leads = db_manager.match_leads_graph_rag(business_id, top_k=6)

        # Record telemetry event for this synthesis run
        telemetry.record_event(
            source="Webhook 1 (Market Ingestion)",
            event_type="SYNTHESIS_EXEC",
            company=matched_leads[0]["company"] if matched_leads else "Market Feed",
            details=f"Synthesized {len(matched_leads)} GraphRAG leads for {primary_match.get('name', 'Niche')}",
            signal_strength="Verified Match"
        )

        elapsed = round(time.time() - start_time, 2)
        return {
            "status": "success",
            "business_id": business_id,
            "execution_time_seconds": elapsed,
            "primary_taxonomy_match": primary_match,
            "confirmed_personas": personas,
            "confirmed_vendor_needs": vendor_needs,
            "target_lead_profile": lead_profile,
            "top_matched_leads": matched_leads,
            "graph_summary": {
                "nodes_connected": inserted_count,
                "multi_hop_traversal": "(:Business)-[:TARGETS_NICHE]->(:BusinessType)-[:REQUIRES_VENDOR]->(:VendorNeed)<-[:EXHIBITS_INTENT]-(:Lead)",
                "graph_engine": "Neo4j Cypher Traversal" if db_manager.verify_connection() else "GraphRAG In-Memory Graph"
            }
        }

    except Exception as e:
        logger.error(f"Lead synthesis pipeline failed: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Lead synthesis failed: {str(e)}")


@app.post("/api/leads/outreach", tags=["AI Outreach Generator"])
def generate_lead_outreach(payload: OutreachRequest):
    """
    1-Click AI Personalized Cold Email & LinkedIn InMail Generator for a specific lead.
    """
    try:
        pitch = generate_outreach_pitch(
            lead=payload.lead,
            founder_vision=payload.founder_vision or "",
            vendor_need=payload.vendor_need or payload.lead.get("vendor_need_match", "")
        )
        return {
            "status": "success",
            "lead_id": payload.lead.get("id"),
            "lead_name": payload.lead.get("name"),
            "company": payload.lead.get("company"),
            "outreach": pitch
        }
    except Exception as e:
        logger.error(f"Outreach generation failed: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate outreach pitch: {str(e)}")


# --- CONTINUOUS DUAL-WEBHOOK ENDPOINTS ---

@app.post("/api/webhooks/market-signals", tags=["Webhooks"])
def ingest_market_signals_webhook(payload: WebhookSignalRequest):
    """
    Webhook 1: Continuous Market & Signal Ingestion.
    Ingests live job postings, funding rounds, domain registrations, and tech migrations.
    """
    evt = telemetry.record_event(
        source=payload.source or "Webhook 1 (Market Ingestion)",
        event_type=payload.signal_type,
        company=payload.company,
        details=payload.details,
        signal_strength=payload.signal_strength or "High"
    )
    return {"status": "received", "event": evt}

@app.post("/api/webhooks/enrichment", tags=["Webhooks"])
def ingest_lead_enrichment_webhook(payload: WebhookEnrichmentRequest):
    """
    Webhook 2: Continuous Lead Enrichment & Verification.
    Ingests executive contact verification, MX/SMTP status, and intent deliverability.
    """
    evt = telemetry.record_event(
        source="Webhook 2 (Lead Enrichment)",
        event_type="ENRICHMENT_VERIFIED",
        company=payload.company,
        details=f"{payload.details} (Deliverability: {payload.deliverability}%)",
        signal_strength="Verified"
    )
    return {"status": "enriched", "event": evt}

@app.get("/api/telemetry/feed", tags=["Telemetry"])
def get_live_telemetry_feed(limit: int = 12):
    """Fetches recent stream of events from Webhook 1 & Webhook 2 for the live ticker."""
    return {
        "status": "active",
        "live_stream": telemetry.get_recent_events(limit=limit)
    }


# --- HEALTH & COMPATIBILITY ENDPOINTS ---

@app.get("/api/health", tags=["Health"])
def health_check():
    """Verify system readiness, Neo4j / Azure VM connectivity, and 200 taxonomy status."""
    neo4j_ok = db_manager.verify_connection()
    groq_ok = bool(os.getenv("GROQ_API_KEY") and os.getenv("GROQ_API_KEY") != "your_groq_api_key_here")

    return {
        "status": "healthy",
        "database": {
            "type": "Neo4j Graph Database (Local / Azure VM)",
            "status": "connected" if neo4j_ok else "in_memory_graph_fallback",
            "uri": os.getenv("NEO4J_URI", "bolt://localhost:7687"),
            "azure_vm_configured": "localhost" not in os.getenv("NEO4J_URI", "localhost")
        },
        "ai_engine": {
            "provider": "Groq API",
            "model": os.getenv("GROQ_MODEL", "llama3-70b-8192"),
            "api_key_configured": groq_ok
        },
        "taxonomy": {
            "status": "loaded",
            "business_types_count": len(taxonomy_engine.business_types),
            "categories_count": len(taxonomy_engine.categories)
        }
    }

# Backward compatibility with test_pipeline.py
@app.post("/api/business/swipe", response_model=SwipeResponse, tags=["Compatibility"])
def record_business_swipe(payload: SwipeRequest):
    db_manager.save_business_swipe(business_id=payload.business_id, swiped_cards=payload.swiped_cards)
    return SwipeResponse(
        status="success",
        message="Business swipe interests successfully updated in Neo4j graph.",
        business_id=payload.business_id,
        swiped_cards=payload.swiped_cards
    )

@app.post("/api/leads/discover", tags=["Compatibility"])
def discover_leads_compat(payload: DiscoverRequest):
    return synthesize_leads_pipeline(SynthesizeRequest(
        business_id=payload.business_id,
        vision_prompt="B2B Software & AI Automation Enterprise",
        swiped_cards=["AI", "SaaS", "B2B", "Enterprise"],
        use_live_scraper=payload.use_live_scraper,
        target_url=payload.target_url
    ))


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    logger.info(f"Starting SignalMind Full-Stack Server on port {port}...")
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
