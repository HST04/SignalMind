# SignalMind Data & Context Workspace

This directory contains the dataset, context specification, and data management scripts for the **SignalMind** AI lead generation platform.

> [!NOTE]
> All work in this directory is isolated from the landing page development files in the root folder (`stitch_landing_page.html` and `assets/`).

## Directory Contents

- **`business_types.json`**: The complete database of 200 curated business types covering 12 major industry verticals with buyer personas, sales cycles, GraphRAG nodes, and lead generation channels.
- **`PROJECT_CONTEXT.md`**: The master project context document for AI agents, outlining SignalMind's value proposition, core user journey, GraphRAG architecture, and dual webhook pipelines.
- **`generate_all_200.py`**: Python script used to construct and serialize the 200 business types database.
- **`verify_data.py`**: Automated validation script to check JSON schema completeness, ID uniqueness, and category distribution.

## Quick Commands

To verify database integrity:
```bash
python data/verify_data.py
```
