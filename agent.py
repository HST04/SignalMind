"""
agent.py - Groq AI Decision Agent & Intelligent Lead Outreach Generator for SignalMind
--------------------------------------------------------------------------------------
This module handles:
1. Integration with Groq API using `groq` Python SDK (`llama3-70b-8192`).
2. Prompt engineering to translate founder vision and taxonomy matches into structured B2B lead profiles.
3. 1-Click AI Personalized Cold Email and LinkedIn Pitch generation for matched leads.
4. Heuristic fallbacks when Groq API key is absent or rate-limited.
"""

import os
import json
import logging
import re
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("signalmind.agent")
logger.setLevel(logging.INFO)

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-70b-8192")

_groq_client = None

def get_groq_client():
    global _groq_client
    if _groq_client is None and GROQ_API_KEY and GROQ_API_KEY != "your_groq_api_key_here":
        try:
            from groq import Groq
            _groq_client = Groq(api_key=GROQ_API_KEY)
            logger.info(f"Initialized Groq SDK client with model '{GROQ_MODEL}'")
        except Exception as e:
            logger.warning(f"Failed to initialize Groq client: {e}")
            _groq_client = None
    return _groq_client


def generate_lead_profile(business_context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Step B (Groq Decision Engine):
    Analyze founder vision, taxonomy nodes, buyer personas, and vendor needs
    to produce a structured B2B lead profile.
    """
    swiped_cards = business_context.get("swiped_cards", [])
    prompt_vision = business_context.get("vision_prompt", "")
    primary_taxonomy = business_context.get("primary_match", {})
    taxonomy_personas = business_context.get("personas", [])
    taxonomy_vendor_needs = business_context.get("vendor_needs", [])

    context_summary = f"Founder Vision: {prompt_vision or 'Not specified'}. "
    if primary_taxonomy:
        context_summary += f"Target Business Type: {primary_taxonomy.get('name', '')} ({primary_taxonomy.get('category', '')}). "
    if taxonomy_personas:
        context_summary += f"Suggested Buyer Personas: {', '.join(taxonomy_personas[:4])}. "
    if taxonomy_vendor_needs:
        context_summary += f"Vendor Needs: {', '.join(taxonomy_vendor_needs[:4])}. "
    if swiped_cards:
        context_summary += f"Interests/Tags: {', '.join(swiped_cards)}."

    prompt = f"""You are SignalMind's B2B Lead Intelligence AI Agent.
Analyze the following founder vision and taxonomy context:
{context_summary}

Generate a valid, strict JSON object describing the ideal B2B lead target profile.
The JSON MUST follow this schema exactly without any markdown backticks or commentary:
{{
  "target_titles": ["List of 3-5 specific decision maker titles, e.g., VP of Operations, CTO"],
  "target_industry": "Primary industry sector matching the niche",
  "search_keywords": ["4-6 specific pain point or technology keywords"],
  "ideal_company_size": "e.g., 20-500 employees",
  "value_proposition_match": "1-2 sentence explanation of why this target profile needs the founder's solution"
}}
"""

    client = get_groq_client()
    if client:
        try:
            logger.info("Querying Groq LLM for target lead profile...")
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a B2B sales intelligence AI. Respond ONLY in valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                model=GROQ_MODEL,
                temperature=0.2,
                max_tokens=600,
            )
            content = chat_completion.choices[0].message.content.strip()
            parsed = parse_json_from_llm(content)
            if parsed:
                return parsed
        except Exception as e:
            logger.warning(f"Groq API call failed ({e}). Using intelligent fallback.")

    # High-quality fallback using extracted taxonomy nodes
    return fallback_lead_profile(business_context)


def fallback_lead_profile(context: Dict[str, Any]) -> Dict[str, Any]:
    """Generates an intelligent lead profile grounded in the 200 business taxonomy."""
    primary = context.get("primary_match", {})
    personas = context.get("personas") or primary.get("ideal_buyer_personas") or ["Chief Technology Officer (CTO)", "VP of Operations", "Managing Director"]
    vendor_needs = context.get("vendor_needs") or primary.get("graph_nodes", {}).get("common_vendor_needs") or ["Software Automation", "Workflow Modernization"]
    industry = primary.get("category") or "B2B Technology & Software Solutions"
    sub_cat = primary.get("sub_category") or primary.get("name") or "Specialized Services"
    keywords = list(set((primary.get("search_keywords") or []) + vendor_needs[:3] + ["Automation", "Workflow"]))[:6]

    return {
        "target_titles": personas[:4],
        "target_industry": f"{industry} — {sub_cat}",
        "search_keywords": keywords,
        "ideal_company_size": "15-500 employees",
        "value_proposition_match": f"Targeting {', '.join(personas[:2])} in {primary.get('name', 'their industry')} seeking solutions for {vendor_needs[0] if vendor_needs else 'workflow efficiency'}."
    }


def generate_outreach_pitch(lead: Dict[str, Any], founder_vision: str = "", vendor_need: str = "") -> Dict[str, str]:
    """
    Generate tailored 1-Click Cold Email and LinkedIn outreach copy for a matched lead.
    """
    lead_name = lead.get("name", "Executive")
    first_name = lead_name.split()[0] if lead_name else "there"
    lead_title = lead.get("title", "Leader")
    company = lead.get("company", "your company")
    trigger = lead.get("trigger_reason") or lead.get("bio") or "recent market expansion"
    vendor_focus = vendor_need or (lead.get("keywords", ["operational growth"])[0] if lead.get("keywords") else "operational efficiency")

    client = get_groq_client()
    if client:
        try:
            prompt = f"""Write a hyper-personalized, concise B2B cold email and LinkedIn message from a founder to a prospective client.
Recipient: {lead_name}, {lead_title} at {company}.
Trigger / Intent Signal: {trigger}
Vendor Need / Pain Point: {vendor_focus}
Founder Solution Context: {founder_vision or 'B2B automation software designed to remove manual bottlenecks'}

Respond ONLY with valid JSON:
{{
  "email_subject": "Catchy, low-friction subject line under 6 words",
  "email_body": "3-4 concise, personalized sentences with a soft CTA (no hard pitch)",
  "linkedin_pitch": "Under 300 character direct InMail message"
}}"""
            chat = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a master B2B copywriter. Respond ONLY in valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                model=GROQ_MODEL,
                temperature=0.3,
                max_tokens=500
            )
            res = parse_json_from_llm(chat.choices[0].message.content.strip())
            if res and "email_subject" in res and "email_body" in res:
                return res
        except Exception as e:
            logger.warning(f"Groq pitch generation failed: {e}")

    # High-converting heuristic outreach template
    return {
        "email_subject": f"Quick thought regarding {company}'s {vendor_focus}",
        "email_body": (
            f"Hi {first_name},\n\n"
            f"Saw {company}'s recent signals around {trigger.lower().replace('.', '')}. "
            f"Given your focus as {lead_title}, I imagine keeping overhead lean while addressing {vendor_focus} is a top priority right now.\n\n"
            f"We built an automated system that tackles this directly for leaders in your space—cutting turnaround by ~40% without complex onboarding.\n\n"
            f"Open to a brief 7-minute visual demo this Thursday?"
        ),
        "linkedin_pitch": (
            f"Hi {first_name}, noticed {company}'s momentum in {vendor_focus}. "
            f"We developed a lightweight workflow tool tailored for {lead_title}s to automate this without friction. Worth a quick connection?"
        )
    }


def parse_json_from_llm(text: str) -> Optional[Dict[str, Any]]:
    """Helper function to clean markdown codeblocks and parse JSON from LLM output."""
    try:
        cleaned_text = re.sub(r'```(?:json)?\s*(.*?)\s*```', r'\1', text, flags=re.DOTALL).strip()
        data = json.loads(cleaned_text)
        return data
    except Exception as e:
        logger.warning(f"Failed to parse JSON from LLM output: {e}. Raw content: {text[:100]}...")
    return None
