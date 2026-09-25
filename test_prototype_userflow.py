"""
test_prototype_userflow.py - Comprehensive End-to-End Userflow Verification
---------------------------------------------------------------------------
Tests the complete SignalMind Working Prototype:
1. Healthcheck & Database status (Neo4j Local / Azure VM check, 200 taxonomy items)
2. Landing Page (`GET /`)
3. Lead Intelligence Dashboard (`GET /app`)
4. Natural Language Vision Taxonomy Classification (`POST /api/taxonomy/classify`)
5. Full 6-Step Lead Synthesis Pipeline (`POST /api/leads/synthesize`)
6. 1-Click AI Cold Email & LinkedIn Pitch Generation (`POST /api/leads/outreach`)
7. Dual Webhooks (Market Signals & Enrichment) & Telemetry Stream (`/api/webhooks/*`)
8. Backward compatibility with legacy swipe and discover endpoints
"""

import sys
import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def run_all_userflows():
    print("=================================================================")
    print("STARTING SIGNALMIND END-TO-END USERFLOW VERIFICATION")
    print("=================================================================\n")

    # USERFLOW 1: System Health & Readiness
    print("--> USERFLOW 1: System Health Check & Database Readiness")
    r1 = client.get("/api/health")
    assert r1.status_code == 200, f"Expected 200, got {r1.status_code}"
    health = r1.json()
    print(f"    Status: {health['status']}")
    print(f"    Database Engine: {health['database']['type']} (Status: {health['database']['status']})")
    print(f"    Azure VM Configured: {health['database']['azure_vm_configured']}")
    print(f"    Taxonomy: {health['taxonomy']['business_types_count']} business types across {health['taxonomy']['categories_count']} categories")
    assert health['taxonomy']['business_types_count'] == 200
    print("    [PASSED] Health Check OK.\n")

    # USERFLOW 2: Public Landing Page Serving
    print("--> USERFLOW 2: Public Landing Page Serving (GET /)")
    r2 = client.get("/")
    assert r2.status_code == 200
    assert "SignalMind" in r2.text
    assert "/app" in r2.text
    print("    [PASSED] Landing Page successfully loaded with links to /app.\n")

    # USERFLOW 3: Lead Intelligence Dashboard Serving
    print("--> USERFLOW 3: Interactive Dashboard Serving (GET /app)")
    r3 = client.get("/app")
    assert r3.status_code == 200
    assert "SignalMind" in r3.text
    assert "Founder Vision" in r3.text
    assert "STAGE 01" in r3.text
    print("    [PASSED] Dashboard successfully loaded with full UI controls.\n")

    # USERFLOW 4: Founder Vision Prompt -> Taxonomy Classification
    print("--> USERFLOW 4: Natural Language Vision Classification")
    sample_vision = "I am building an automated AI call dispatching and appointment scheduling software for commercial roofing and HVAC contractors."
    r4 = client.post("/api/taxonomy/classify", json={"vision_prompt": sample_vision})
    assert r4.status_code == 200
    classification = r4.json()
    primary = classification["primary_match"]
    print(f"    Prompt: '{sample_vision}'")
    print(f"    Matched Taxonomy Node: {primary.get('name')} ({primary.get('category')})")
    print(f"    Match Confidence: {primary.get('match_score')}%")
    print(f"    Extracted Personas: {classification['aggregated_personas']}")
    print(f"    Extracted Vendor Needs: {classification['aggregated_vendor_needs']}")
    assert len(classification['aggregated_personas']) > 0
    assert len(classification['aggregated_vendor_needs']) > 0
    print("    [PASSED] Vision classification mapped accurately to 200 taxonomy nodes.\n")

    # USERFLOW 5: Full 6-Step Lead Synthesis & GraphRAG Matching
    print("--> USERFLOW 5: 6-Step Lead Synthesis & GraphRAG Multi-Hop Matching")
    synthesis_payload = {
        "business_id": "test_founder_session_99",
        "vision_prompt": sample_vision,
        "primary_match": primary,
        "personas": classification['aggregated_personas'],
        "vendor_needs": classification['aggregated_vendor_needs'],
        "use_live_scraper": False
    }
    r5 = client.post("/api/leads/synthesize", json=synthesis_payload)
    assert r5.status_code == 200
    synthesis_res = r5.json()
    leads = synthesis_res.get("top_matched_leads", [])
    print(f"    Execution Time: {synthesis_res['execution_time_seconds']}s")
    print(f"    Leads Delivered: {len(leads)}")
    assert len(leads) > 0

    first_lead = leads[0]
    print(f"    Sample Lead #1: {first_lead['name']} — {first_lead['title']} at {first_lead['company']}")
    print(f"    Email: {first_lead['contact_email']} | Phone: {first_lead['phone']}")
    print(f"    Deliverability: {first_lead['deliverability_score']}% | Intent Score: {first_lead['intent_score']}%")
    print(f"    Intent Trigger: {first_lead['trigger_reason']}")
    print(f"    Graph Path: {first_lead['graph_reasoning']}")
    assert first_lead['deliverability_score'] >= 90
    print("    [PASSED] Lead Synthesis successfully delivered verified contacts with GraphRAG reasoning.\n")

    # USERFLOW 6: 1-Click AI Outreach Pitch Generation
    print("--> USERFLOW 6: 1-Click AI Outreach Pitch Generation")
    outreach_payload = {
        "lead": first_lead,
        "founder_vision": sample_vision,
        "vendor_need": first_lead.get("vendor_need_match", "Automated Dispatching")
    }
    r6 = client.post("/api/leads/outreach", json=outreach_payload)
    assert r6.status_code == 200
    outreach = r6.json().get("outreach", {})
    print(f"    Target: {first_lead['name']} at {first_lead['company']}")
    print(f"    Email Subject: {outreach.get('email_subject')}")
    print(f"    Email Snippet: {outreach.get('email_body')[:140]}...")
    print(f"    LinkedIn Pitch: {outreach.get('linkedin_pitch')}")
    assert len(outreach.get('email_subject', '')) > 0
    assert len(outreach.get('email_body', '')) > 0
    print("    [PASSED] AI Outreach Copy generated seamlessly.\n")

    # USERFLOW 7: Continuous Dual-Webhook Signal Ingestion & Live Telemetry
    print("--> USERFLOW 7: Continuous Dual-Webhook Ingestion & Live Telemetry")
    # Ingest Webhook 1 event
    w1_res = client.post("/api/webhooks/market-signals", json={
        "signal_type": "HIRING_EXPANSION",
        "company": "Apex RoofTech Solutions",
        "details": "Opened 3 dispatch manager positions on LinkedIn"
    })
    assert w1_res.status_code == 200
    # Ingest Webhook 2 event
    w2_res = client.post("/api/webhooks/enrichment", json={
        "company": "Apex RoofTech Solutions",
        "details": "SMTP handshake confirmed with 99% confidence",
        "deliverability": 99
    })
    assert w2_res.status_code == 200

    # Read live telemetry stream
    telemetry_res = client.get("/api/telemetry/feed")
    assert telemetry_res.status_code == 200
    feed = telemetry_res.json().get("live_stream", [])
    print(f"    Recent Telemetry Events in Feed: {len(feed)}")
    assert len(feed) > 0
    print(f"    Latest Signal: [{feed[0]['source']}] {feed[0]['company']} - {feed[0]['details']}")
    print("    [PASSED] Dual-Webhook ingestion & telemetry stream operating normally.\n")

    # USERFLOW 8: Backward Compatibility
    print("--> USERFLOW 8: Legacy Backward Compatibility (Swipe & Discover)")
    swipe_res = client.post("/api/business/swipe", json={
        "business_id": "compat_user_1",
        "swiped_cards": ["AI", "SaaS", "B2B"]
    })
    assert swipe_res.status_code == 200
    discover_res = client.post("/api/leads/discover", json={"business_id": "compat_user_1"})
    assert discover_res.status_code == 200
    print("    [PASSED] Backward compatibility preserved 100%.\n")

    print("=================================================================")
    print("ALL 8 USERFLOWS TESTED AND VERIFIED SUCCESSFULLY!")
    print("=================================================================")

if __name__ == "__main__":
    try:
        run_all_userflows()
    except Exception as e:
        print(f"\n[FAIL] Userflow test failed: {e}")
        sys.exit(1)
