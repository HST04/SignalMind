# SignalMind — AI-Driven Hyper-Targeted Lead Generation Platform

> **Version:** 2.0.0 (Unified Full-Stack Working Prototype)  
> **Backend:** FastAPI, SentenceTransformers (`all-MiniLM-L6-v2`), Neo4j Graph DB / High-Performance In-Memory Graph, Groq LLM (`llama3-70b-8192`)  
> **Frontend:** Obsidian Liquid-Glass Design System, Tailwind CSS, Lucide Icons  
> **Taxonomy:** 200 Curated B2B Business Types across 12 Industry Verticals (`data/business_types.json`)

---

## Executive Summary

SignalMind allows modern founders and growth teams to simply **describe the business they are building in natural language**. SignalMind parses their vision, accurately classifies the niche across a 200-business taxonomy, and queries a dynamic **GraphRAG (Graph Retrieval-Augmented Generation)** knowledge graph powered by continuous dual webhooks to deliver hyper-targeted, high-converting leads with 1-click personalized AI outreach.

---

## Key Features

1. **Natural Language Vision Classifier:**
   - Input your startup or agency concept in freeform English.
   - Maps intent against 200 curated business types in `data/business_types.json`.
   - Automatically extracts target buyer personas, common vendor needs (pain points), typical ticket sizes, and sales cycles.

2. **GraphRAG Multi-Hop Lead Engine:**
   - Traverses knowledge graph relationships:  
     `(:Business)-[:TARGETS_NICHE]->(:BusinessType)-[:REQUIRES_VENDOR]->(:VendorNeed)<-[:EXHIBITS_INTENT]-(:Lead)`
   - Vector similarity search combined with graph relationship scoring.
   - Runs on local/remote Neo4j or seamless built-in In-Memory Graph Engine.

3. **Continuous Dual-Webhook Telemetry:**
   - **Webhook 1 (Market Ingestion):** Ingests live job postings, funding alerts, tech stack migrations, and newly registered domains.
   - **Webhook 2 (Lead Enrichment):** Ingests executive verification signals, SMTP/MX deliverability scores, and direct dials.
   - Live stream ticker in the web interface showing real-time market intent signals.

4. **1-Click AI Outreach Pitch Generator:**
   - Generates tailored, high-converting cold email (Subject + Body) and LinkedIn InMail notes specifically addressing the lead's company and intent trigger.

5. **Export Suite:**
   - 1-click browser export to **CSV** and **JSON**.

---

## Architecture: Multi-Page Flow

- **`/` — Primary 3D Scrollytelling Showcase (`index.html`):**  
  Obsidian liquid-glass experience with interactive vision context dock, Three.js parametric botanical visualization, 4 scroll story beats, 200 taxonomy category explorer, and live telemetry preview.

- **`/app` — Interactive Lead Intelligence Studio (`app.html`):**  
  Full working studio with vision input, intelligent presets (Roofing, Dental, CFO, Solar, Legal), interactive taxonomy & vendor need dissection, live lead cards, AI outreach modal, and CSV/JSON export.

- **`/landing` — High-Performance Marketing Showcase (`landing.html`):**  
  Streamlined liquid-glass landing page with instant sandbox classification and direct studio entry.


---

## Quickstart Guide

### 1. Activate Virtual Environment & Install Dependencies
```bash
# In Windows PowerShell:
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Launch the Unified Full-Stack Prototype
```bash
.\venv\Scripts\python.exe main.py
```
Or with Uvicorn:
```bash
uvicorn main:app --reload --port 8000
```

### 3. Open in Browser
- **Landing Page:** [http://localhost:8000/](http://localhost:8000/)
- **Lead Intelligence App:** [http://localhost:8000/app](http://localhost:8000/app)
- **Interactive API Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Connecting to an Azure VM (Neo4j)

SignalMind automatically runs in high-performance **In-Memory Graph Fallback mode** with zero configuration required.

If you have **Azure for Students credits** and wish to connect a live distributed Neo4j instance on an Azure VM:
1. Follow the step-by-step instructions in [`AZURE_VM_SETUP.md`](./AZURE_VM_SETUP.md).
2. Configure `.env`:
   ```env
   NEO4J_URI=bolt://<YOUR_AZURE_VM_PUBLIC_IP>:7687
   NEO4J_USER=neo4j
   NEO4J_PASSWORD=YourPassword123!
   ```
3. Restart `main.py`. The top status pill in `/app` will automatically show `Azure VM Neo4j: connected`.

---

## Automated Verification Suite
 
Run the master end-to-end regression and verification suite:
```bash
.\venv\Scripts\python.exe verify_all.py
```

Run the full end-to-end userflow test suite:
```bash
.\venv\Scripts\python.exe test_prototype_userflow.py
```

Run the comprehensive API & edge cases test:
```bash
.\venv\Scripts\python.exe comprehensive_manual_test.py
```

Run the backend pipeline unit test:
```bash
.\venv\Scripts\python.exe test_pipeline.py
```

Validate the 200-business taxonomy integrity:
```bash
.\venv\Scripts\python.exe data/verify_data.py
```


---

## REST API Overview

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves public landing page |
| `GET` | `/app` | Serves interactive lead intelligence app |
| `POST` | `/api/taxonomy/classify` | Classifies founder vision against 200 taxonomy nodes |
| `GET` | `/api/taxonomy/categories` | Returns 12 industry categories with counts |
| `POST` | `/api/leads/synthesize` | Full 6-step GraphRAG lead synthesis pipeline |
| `POST` | `/api/leads/outreach` | 1-Click AI Cold Email and LinkedIn Pitch generator |
| `POST` | `/api/webhooks/market-signals` | Webhook 1: Market & web signal ingestion |
| `POST` | `/api/webhooks/enrichment` | Webhook 2: Lead enrichment & verification ingestion |
| `GET` | `/api/telemetry/feed` | Real-time dual webhook telemetry stream |
| `GET` | `/api/health` | System readiness & Azure VM Neo4j connectivity check |
