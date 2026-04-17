#!/usr/bin/env python3
from pathlib import Path
import sys

required = [
    "README.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "Conditional_Final_Wall_Index.tex",
    "PROGRAM_STATUS.tex",
    "docs",
    "infra",
]

missing = [p for p in required if not Path(p).exists()]
if missing:
    print({"valid": False, "missing": missing})
    sys.exit(1)

readme = Path("README.md").read_text(errors="ignore").lower()

checks = {
    "mentions_conditional_index": "conditional index" in readme or "final-wall-conditional-index" in readme,
    "mentions_auditability_or_disclosure": (
        "auditability" in readme or "disclosure" in readme or "transparency" in readme
    ),
    "mentions_no_proofs": "no proofs" in readme,
    "mentions_update_policy": "update policy" in readme,
    "mentions_relationship_to_other_repositories": "relationship to other repositories" in readme,
}

failed = [k for k, v in checks.items() if not v]
if failed:
    print({"valid": False, "failed_checks": failed, "checks": checks})
    sys.exit(1)

print({"valid": True, "checked": required, "checks": checks})
