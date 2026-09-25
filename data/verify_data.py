import json

with open("e:/SignalMind/data/business_types.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data.get("business_types", [])
print(f"Total count reported in JSON: {data.get('total_count')}")
print(f"Actual items count in array: {len(items)}")

ids = set()
duplicates = []
categories = {}

required_keys = [
    "id", "name", "category", "sub_category", "business_model", "description",
    "target_audience", "ideal_buyer_personas", "lead_generation_channels",
    "typical_ticket_size", "sales_cycle", "graph_nodes", "search_keywords"
]

missing_keys = []

for idx, item in enumerate(items):
    item_id = item.get("id")
    if item_id in ids:
        duplicates.append(item_id)
    ids.add(item_id)
    
    cat = item.get("category", "Unknown")
    categories[cat] = categories.get(cat, 0) + 1
    
    for k in required_keys:
        if k not in item or item[k] is None:
            missing_keys.append((idx, item_id, k))

print("\n--- VALIDATION RESULTS ---")
print(f"Unique IDs count: {len(ids)}")
print(f"Duplicate IDs: {duplicates}")
print(f"Missing schema keys count: {len(missing_keys)}")
print("\nCategory Breakdown:")
for cat, count in categories.items():
    print(f"  - {cat}: {count} business types")

if len(items) == 200 and len(ids) == 200 and len(missing_keys) == 0:
    print("\n[SUCCESS] VALIDATION PASSED: 100% compliant with 200 unique, well-formed business types!")
else:
    print("\n[FAILURE] VALIDATION FAILED! Check issues above.")
