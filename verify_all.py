"""
verify_all.py - SignalMind Master End-to-End Verification & Health Suite
-------------------------------------------------------------------------
Runs all automated and manual verification suites:
1. 200 Taxonomy Schema & Completeness (data/verify_data.py)
2. DOM Element & JS ID Integrity (test_dom_elements.py)
3. Backend Graph Pipeline Unit Test (test_pipeline.py)
4. Comprehensive API Endpoints & Edge Cases (comprehensive_manual_test.py)
5. Prototype End-to-End 8 Userflows (test_prototype_userflow.py)
"""

import sys
import subprocess
import time

def run_step(step_name, command):
    print(f"\n=================================================================")
    print(f"RUNNING: {step_name}")
    print(f"Command: {' '.join(command)}")
    print(f"=================================================================")
    start = time.time()
    res = subprocess.run(command, capture_output=True, text=True)
    elapsed = round(time.time() - start, 2)
    print(res.stdout)
    if res.returncode != 0:
        print(f"[FAIL] {step_name} FAILED in {elapsed}s (Exit code: {res.returncode}):")
        print(res.stderr)
        return False
    print(f"[PASS] {step_name} PASSED in {elapsed}s\n")
    return True

def main():
    py = sys.executable
    print("#################################################################")
    print("      SIGNALMIND MASTER VERIFICATION & REGRESSION SUITE          ")
    print("#################################################################")

    steps = [
        ("Step 1: 200 Business Taxonomy Integrity", [py, "data/verify_data.py"]),
        ("Step 2: DOM Elements & ID Mapping Verification", [py, "test_dom_elements.py"]),
        ("Step 3: JavaScript Engine Syntax Validation", ["node", "-e", """
const fs = require('fs');
const vm = require('vm');
['index.html', 'app.html', 'landing.html'].forEach(f => {
  const content = fs.readFileSync(f, 'utf8');
  const reg = /<script(?![^>]*\\bsrc\\b)[^>]*>([\\s\\S]*?)<\\/script>/gi;
  let m;
  while ((m = reg.exec(content)) !== null) {
    if (m[1].trim()) new vm.Script(m[1], { filename: f });
  }
  console.log('Validated JS syntax in ' + f + ': OK');
});
""" ]),
        ("Step 4: Comprehensive API Endpoints & Edge Cases", [py, "comprehensive_manual_test.py"]),

        ("Step 5: Backend GraphRAG Pipeline Unit Test", [py, "test_pipeline.py"]),
        ("Step 6: Prototype End-to-End 8 Userflows", [py, "test_prototype_userflow.py"]),
    ]

    failed = []
    for name, cmd in steps:
        ok = run_step(name, cmd)
        if not ok:
            failed.append(name)

    print("#################################################################")
    if failed:
        print(f"[FAIL] VERIFICATION COMPLETED WITH {len(failed)} FAILURE(S):")
        for f in failed:
            print(f"  - {f}")
        sys.exit(1)
    else:
        print("[SUCCESS] ALL 6 SUITES PASSED! ZERO REGRESSIONS, ALL GAPS BRIDGED.")
        print("#################################################################")

if __name__ == "__main__":
    main()
