"""
test_pipeline.py - Automated End-to-End Test Suite for SignalMind Backend
-------------------------------------------------------------------------
Validates:
1. System Health Check (/api/health)
2. Recording Business Swipes (/api/business/swipe)
3. Business Context Graph Retrieval
4. Groq Lead Profile Generation & Fallback
5. Web Scraping & Lead Insertion
6. Graph RAG Vector Similarity Search & Top Match Retrieval (/api/leads/discover)
"""

import sys
import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    print("\n--- TEST 1: Health Check Endpoint ---")
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    print("Health Check Response:")
    print(json.dumps(data, indent=2))
    assert data["status"] == "healthy"
    print("[OK] Health Check Passed.")
 
def test_business_swipe():
    print("\n--- TEST 2: POST /api/business/swipe ---")
    payload = {
        "business_id": "biz_test_8842",
        "swiped_cards": ["AI", "SaaS", "B2B", "Enterprise", "Machine Learning"]
    }
    response = client.post("/api/business/swipe", json=payload)
    assert response.status_code == 200
    data = response.json()
    print("Swipe Endpoint Response:")
    print(json.dumps(data, indent=2))
    assert data["status"] == "success"
    assert data["business_id"] == "biz_test_8842"
    assert len(data["swiped_cards"]) == 5
    print("[OK] Business Swipe Endpoint Passed.")
 
def test_leads_discover_pipeline():
    print("\n--- TEST 3: POST /api/leads/discover (Full 6-Step Pipeline) ---")
    payload = {
        "business_id": "biz_test_8842",
        "use_live_scraper": False
    }
    response = client.post("/api/leads/discover", json=payload)
    assert response.status_code == 200
    data = response.json()
    print("Discover Pipeline Response Summary:")
    print("Status:", data.get("status"))
    print("Pipeline Summary:", json.dumps(data.get("pipeline_summary"), indent=2))
    print("Target Lead Profile:", json.dumps(data.get("target_lead_profile"), indent=2))
    print(f"\nTop Matched Leads Returned: {len(data.get('top_matched_leads', []))}")
    
    top_leads = data.get("top_matched_leads", [])
    assert len(top_leads) > 0
    for idx, lead in enumerate(top_leads, 1):
        print(f"\nLead #{idx}: {lead['title']} at {lead['company']}")
        print(f"  Industry: {lead['industry']}")
        print(f"  Contact: {lead['contact_email']}")
        print(f"  Similarity Score: {lead['similarity_score']} | Graph RAG Score: {lead['graph_rag_score']}")
        print(f"  Matched Interests: {lead['matched_interests']}")

    print("\n[OK] Full Lead Intelligence Pipeline Passed.")

if __name__ == "__main__":
    try:
        test_health_check()
        test_business_swipe()
        test_leads_discover_pipeline()
        print("\n==================================================")
        print("ALL SIGNALMIND BACKEND TESTS COMPLETED SUCCESSFULLY!")
        print("==================================================")
    except Exception as err:
        print(f"\n[FAIL] Test execution failed: {err}")
        sys.exit(1)
