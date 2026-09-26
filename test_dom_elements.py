import re

for filename in ['index.html', 'app.html', 'landing.html']:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()

        ids_in_dom = set(re.findall(r'id=["\']([^"\']+)["\']', html))
        ids_in_js = set(re.findall(r'getElementById\(["\']([^"\']+)["\']\)', html))

        missing = ids_in_js - ids_in_dom
        print(f"=== {filename} ===")
        print(f"DOM IDs found: {len(ids_in_dom)}")
        print(f"JS getElementById calls: {len(ids_in_js)}")
        if missing:
            print(f"MISSING IDs referenced in JS: {missing}")
        else:
            print("All getElementById targets exist in DOM!")
    except Exception as e:
        print(f"Error checking {filename}: {e}")
