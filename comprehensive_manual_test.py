"""
comprehensive_manual_test.py - Deep Manual Testing of Every Component & Edge Case
"""
import sys
import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_all():
    errors = []
    print("=================================================================")
    print("RUNNING EXHAUSTIVE MANUAL TEST SUITE ACROSS ALL ENDPOINTS")
    print("=================================================================\n")

    # 1. Health Endpoint
    print("--- 1. Testing /api/health ---")
    try:
        r = client.get("/api/health")
        assert r.status_code == 200
        d = r.json()
        assert d["status"] == "healthy"
        assert d["taxonomy"]["business_types_count"] == 200
        print("  [OK] /api/health passed")
    except Exception as e:
        errors.append(f"/api/health failed: {e}")
        print(f"  [FAIL] {e}")

    # 2. Web Pages
    print("\n--- 2. Testing Web Page Endpoints ---")
    for path, expected_text in [("/", "SignalMind"), ("/app", "SignalMind"), ("/landing", "SignalMind"), ("/docs", "Swagger UI")]:
        try:
            r = client.get(path)
            assert r.status_code == 200
            assert expected_text in r.text
            print(f"  [OK] {path} served with '{expected_text}'")
        except Exception as e:
            errors.append(f"Page {path} failed: {e}")
            print(f"  [FAIL] {path}: {e}")


    # 3. Taxonomy Categories
    print("\n--- 3. Testing /api/taxonomy/categories ---")
    try:
        r = client.get("/api/taxonomy/categories")
        assert r.status_code == 200
        cats = r.json().get("categories", [])
        assert len(cats) == 12
        total = sum(c["count"] for c in cats)
        assert total == 200
        print(f"  [OK] 12 categories verified with exactly 200 total business types")
    except Exception as e:
        errors.append(f"/api/taxonomy/categories failed: {e}")
        print(f"  [FAIL] {e}")

    # 4. Taxonomy Search
    print("\n--- 4. Testing /api/taxonomy/search ---")
    test_queries = ["roofing", "dental", "cfo", "solar", "law", "saas", "", "xyzunknownnonexistent123"]
    for q in test_queries:
        try:
            r = client.get(f"/api/taxonomy/search?q={q}&limit=4")
            assert r.status_code == 200
            res = r.json().get("results", [])
            print(f"  [OK] Search '{q}' returned {len(res)} results (Top match: {res[0]['name'] if res else 'None'})")
        except Exception as e:
            errors.append(f"Search '{q}' failed: {e}")
            print(f"  [FAIL] Search '{q}': {e}")

    # 5. Taxonomy Classify (Valid, Edge cases, Empty)
    print("\n--- 5. Testing /api/taxonomy/classify ---")
    # Empty prompt (expect 400)
    r_empty = client.post("/api/taxonomy/classify", json={"vision_prompt": "   "})
    assert r_empty.status_code == 400, f"Expected 400 on empty prompt, got {r_empty.status_code}"
    print("  [OK] Empty prompt rejected with 400 as expected")

    # Valid presets
    test_visions = [
        "Automated AI call dispatching software for roofing and HVAC contractors",
        "Clinical voice documentation AI for dental practice clinics",
        "Fractional CFO cash flow runway modeling for Series A startups",
        "Solar permit automated CAD drafting tool",
        "Commercial corporate law contract review and diligence assistant",
        "A boutique pet grooming salon booking mobile app in Chicago"
    ]
    for v in test_visions:
        try:
            r = client.post("/api/taxonomy/classify", json={"vision_prompt": v})
            assert r.status_code == 200
            data = r.json()
            primary = data["primary_match"]
            assert primary is not None
            assert len(data["aggregated_personas"]) > 0
            assert len(data["aggregated_vendor_needs"]) > 0
            print(f"  [OK] Classified: '{v[:40]}...' -> {primary['name']} ({primary['match_score']}%)")
        except Exception as e:
            errors.append(f"Classify '{v}' failed: {e}")
            print(f"  [FAIL] {e}")

    # 6. Lead Synthesis Pipeline (with & without primary_match, personas, vendor_needs)
    print("\n--- 6. Testing /api/leads/synthesize ---")
    try:
        # Empty prompt check (expect 400)
        r_synth_empty = client.post("/api/leads/synthesize", json={"vision_prompt": ""})
        assert r_synth_empty.status_code == 400
        print("  [OK] /api/leads/synthesize rejects empty vision_prompt with 400")

        # Minimal payload: only vision_prompt
        r_min = client.post("/api/leads/synthesize", json={
            "vision_prompt": "Automated AI call dispatching software for commercial roofing contractors"
        })
        assert r_min.status_code == 200
        d_min = r_min.json()
        assert len(d_min["top_matched_leads"]) > 0
        print(f"  [OK] Minimal payload synthesis returned {len(d_min['top_matched_leads'])} leads")


        # Full payload
        r_full = client.post("/api/leads/synthesize", json={
            "business_id": "manual_test_biz_1",
            "vision_prompt": "Fractional CFO advisory platform with cash runway simulation",
            "primary_match": {"name": "Fractional CFO Advisory", "category": "Financial Services"},
            "personas": ["Chief Executive Officer", "Founder", "VP of Finance"],
            "vendor_needs": ["Runway Modeling", "Audit Compliance"],
            "swiped_cards": ["CFO", "Fintech", "SaaS"]
        })
        assert r_full.status_code == 200
        d_full = r_full.json()
        leads = d_full["top_matched_leads"]
        assert len(leads) > 0
        lead1 = leads[0]
        assert "name" in lead1 and "contact_email" in lead1 and "phone" in lead1
        assert "graph_rag_score" in lead1 and "similarity_score" in lead1
        print(f"  [OK] Full payload synthesis returned {len(leads)} leads. Lead #1: {lead1['name']} ({lead1['company']})")
    except Exception as e:
        errors.append(f"Synthesis failed: {e}")
        print(f"  [FAIL] {e}")

    # 7. AI Outreach Generator
    print("\n--- 7. Testing /api/leads/outreach ---")
    sample_lead = {
        "id": "lead_test_01",
        "name": "Marcus Sterling",
        "title": "VP of Operations",
        "company": "Titan Commercial Roofing",
        "trigger_reason": "Hiring 3 dispatch coordinators on LinkedIn",
        "vendor_need_match": "Dispatch Automation Software"
    }
    try:
        # Empty lead check (expect 400)
        r_empty_lead = client.post("/api/leads/outreach", json={"lead": {}})
        assert r_empty_lead.status_code == 400
        print("  [OK] /api/leads/outreach rejects empty lead with 400")

        r_outreach = client.post("/api/leads/outreach", json={
            "lead": sample_lead,
            "founder_vision": "AI call dispatching platform",
            "vendor_need": "Dispatch Automation"
        })
        assert r_outreach.status_code == 200
        outreach_data = r_outreach.json()
        pitch = outreach_data["outreach"]
        assert len(pitch.get("email_subject", "")) > 0
        assert len(pitch.get("email_body", "")) > 0
        assert len(pitch.get("linkedin_pitch", "")) > 0
        print(f"  [OK] Outreach pitch generated successfully:")
        print(f"       Subject: {pitch['email_subject']}")
        print(f"       LinkedIn: {pitch['linkedin_pitch']}")
    except Exception as e:
        errors.append(f"Outreach failed: {e}")
        print(f"  [FAIL] {e}")

    # 8. Webhooks & Telemetry Stream
    print("\n--- 8. Testing Webhooks & Telemetry ---")
    try:
        # Webhook 1
        r_w1 = client.post("/api/webhooks/market-signals", json={
            "signal_type": "FUNDING_ALERT",
            "company": "QuantumScale Tech",
            "details": "Secured $6M Series A funding",
            "signal_strength": "Very High"
        })
        assert r_w1.status_code == 200
        w1_event = r_w1.json()["event"]
        assert w1_event["company"] == "QuantumScale Tech"
        print("  [OK] Webhook 1 accepted market signal")

        # Webhook 2
        r_w2 = client.post("/api/webhooks/enrichment", json={
            "company": "QuantumScale Tech",
            "details": "Verified founder email & direct dial",
            "deliverability": 99
        })
        assert r_w2.status_code == 200
        w2_event = r_w2.json()["event"]
        assert w2_event["company"] == "QuantumScale Tech"
        print("  [OK] Webhook 2 accepted lead enrichment")

        # Telemetry Feed
        r_feed = client.get("/api/telemetry/feed?limit=5")
        assert r_feed.status_code == 200
        feed = r_feed.json()["live_stream"]
        assert len(feed) > 0
        assert feed[0]["company"] == "QuantumScale Tech"
        print(f"  [OK] Live telemetry feed contains {len(feed)} items, latest: {feed[0]['company']}")
    except Exception as e:
        errors.append(f"Webhooks/Telemetry failed: {e}")
        print(f"  [FAIL] {e}")

    # 9. Backward Compatibility
    print("\n--- 9. Testing Backward Compatibility Endpoints ---")
    try:
        r_swipe = client.post("/api/business/swipe", json={
            "business_id": "compat_user",
            "swiped_cards": ["AI", "SaaS"]
        })
        assert r_swipe.status_code == 200
        print("  [OK] /api/business/swipe passed")

        r_disc = client.post("/api/leads/discover", json={
            "business_id": "compat_user"
        })
        assert r_disc.status_code == 200
        print("  [OK] /api/leads/discover passed")
    except Exception as e:
        errors.append(f"Backward compatibility failed: {e}")
        print(f"  [FAIL] {e}")

    print("\n=================================================================")
    if errors:
        print(f"COMPLETED WITH {len(errors)} ERROR(S):")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("ALL ENDPOINT & USERFLOW TESTS PASSED CLEANLY (0 ERRORS)!")
        print("=================================================================")

if __name__ == "__main__":
    test_all()
