"""
telemetry.py - Continuous Dual-Webhook Signal Ingestion & Live Telemetry Stream
-------------------------------------------------------------------------------
This module manages:
1. Webhook 1 (Market Signals): Live web signals, job postings, funding alerts, DNS/domain shifts.
2. Webhook 2 (Lead Enrichment): Executive contact enrichment, MX/SMTP deliverability scoring.
3. In-memory buffer of recent events for frontend live ticker & graph telemetry dashboard.
4. Auto-generator of synthetic real-time telemetry events when running the prototype.
"""

import time
import random
import logging
from typing import List, Dict, Any

logger = logging.getLogger("signalmind.telemetry")
logger.setLevel(logging.INFO)

MAX_BUFFER = 50
_telemetry_events: List[Dict[str, Any]] = []

SAMPLE_SIGNALS = [
    {"source": "Webhook 1 (Market Ingestion)", "type": "JOB_POSTING", "company": "Apex Mechanical Group", "details": "Posted 2 Dispatcher positions on LinkedIn", "signal_strength": "High"},
    {"source": "Webhook 2 (Lead Enrichment)", "type": "MX_VERIFIED", "company": "Veritas Dental Partners", "details": "Direct dial & email deliverability verified (99% score)", "signal_strength": "Verified"},
    {"source": "Webhook 1 (Market Ingestion)", "type": "FUNDING_ALERT", "company": "Titan Skyline Builders", "details": "Closed $3.8M Series Seed expansion", "signal_strength": "Very High"},
    {"source": "Webhook 2 (Lead Enrichment)", "type": "DECISION_MAKER", "company": "Metropolitan Asset Mgmt", "details": "Identified VP of Facilities as primary buyer", "signal_strength": "Enriched"},
    {"source": "Webhook 1 (Market Ingestion)", "type": "TECH_MIGRATION", "company": "Lumina Smile Centers", "details": "Detected migration away from legacy server software", "signal_strength": "Active Intent"},
    {"source": "Webhook 2 (Lead Enrichment)", "type": "DELIVERABILITY_CHECK", "company": "Sterling Advisory", "details": "SMTP handshake confirmed; zero bounce probability", "signal_strength": "Verified"},
    {"source": "Webhook 1 (Market Ingestion)", "type": "DOMAIN_REGISTERED", "company": "Summit Ridge Roofing", "details": "New regional hub domain active: summit-midwest.com", "signal_strength": "Growth"}
]

def record_event(source: str, event_type: str, company: str, details: str, signal_strength: str = "High") -> Dict[str, Any]:
    """Record an incoming webhook event into the live telemetry buffer."""
    event = {
        "id": f"evt_{int(time.time() * 1000)}_{random.randint(100, 999)}",
        "timestamp": time.strftime("%H:%M:%S"),
        "source": source,
        "type": event_type,
        "company": company,
        "details": details,
        "signal_strength": signal_strength
    }
    _telemetry_events.insert(0, event)
    if len(_telemetry_events) > MAX_BUFFER:
        _telemetry_events.pop()
    logger.info(f"Recorded Telemetry Event: [{source}] {company} - {event_type}")
    return event

def get_recent_events(limit: int = 15) -> List[Dict[str, Any]]:
    """Retrieve recent telemetry events for frontend live ticker."""
    if len(_telemetry_events) < 5:
        # Seed initial buffer with rich events
        for item in SAMPLE_SIGNALS:
            record_event(item["source"], item["type"], item["company"], item["details"], item["signal_strength"])
    return _telemetry_events[:limit]
