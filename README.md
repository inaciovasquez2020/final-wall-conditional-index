# final-wall-conditional-index

Authoritative **index of conditional dependencies** for the *Final Wall*.

This repository enumerates **every statement that is currently conditional** in the Final Wall program: assumptions, missing lemmas, witness principles, or inequalities that are required but not yet discharged unconditionally. It is an **index**, not a proof repository.

The purpose is disclosure, auditability, and closure planning.

---

## Scope

* Records **what is still conditional**, exactly and explicitly
* Preserves a **one‑to‑one mapping** between conditionals and the manuscripts / formal artifacts that reference them
* Provides a stable surface for reviewers, collaborators, and future closure work

This repository intentionally contains **no proofs**, **no heuristics**, and **no speculation**.

---

## What this repository is

* A **logical dependency index**
* A **closure checklist** for the Final Wall
* A **transparency artifact** for the program’s current status

## What this repository is not

* A proof of the Final Wall
* A conjecture generator
* A place for exploratory arguments or partial derivations

---

## Contents

```
.
├── Conditional_Final_Wall_Index.tex   # Canonical list of all conditional statements
├── PROGRAM_STATUS.tex                 # Snapshot of program state and dependency count
├── CHANGELOG.md                       # Historical record of additions/removals
└── README.md
```

All authoritative content is maintained in **LaTeX** to allow direct inclusion in manuscripts and referee packages.

---

## Conditional entry format

Each indexed conditional records:

* **Identifier** (stable name)
* **Statement** (formal or semi‑formal)
* **Type** (lemma, inequality, witness, structural assumption)
* **Upstream dependencies** (if any)
* **Downstream usage** (manuscripts / sections)
* **Resolution status** (open / conditional / discharged)

No conditional may appear elsewhere in the program without appearing here.

---

## Usage

### Reviewing the current conditionals

```bash
pdflatex Conditional_Final_Wall_Index.tex
```

This produces a human‑readable PDF listing all remaining conditional dependencies.

### Including in a manuscript

The compiled index may be:

* attached as an appendix,
* cited as a dependency disclosure,
* provided to referees as a separate audit document.

---

## Update policy

This repository follows strict rules:

* **Add** an entry when a new conditional is introduced anywhere in the program
* **Modify** an entry only to clarify scope or references
* **Remove** an entry *only* when an unconditional proof exists, with citation

All changes must preserve historical traceability via `CHANGELOG.md`.

---

## Stability

* The structure of the index is **stable**
* Identifiers are **never reused**
* Past conditionals remain documented even after resolution

This ensures that the logical evolution of the Final Wall remains auditable.

---

## Relationship to other repositories

This index sits **above** formal dependencies and **below** manuscripts:

```
overlap-rigidity-lean      (formal definitions)
        ↓
final-wall-conditional-index   (this repo)
        ↓
manuscripts / claims / proofs
```

No repository above this layer may introduce a conditional without registering it here.

---

## Status

* Purpose: **indexing only**
* Claims: **none**
* Proofs: **none**
* Authority: **canonical for conditionals**

Refer to `PROGRAM_STATUS.tex` for the current count and classification.

---
\section*{License and Usage}

This document is released under the MIT License.

Permission is granted to use, copy, and redistribute this document, with or
without modification, provided that proper attribution to the author is
maintained.

This license applies to the \emph{presentation and distribution} of the
document only. It does not assert the correctness of any result, does not
constitute a claim of proof, and does not alter the explicitly conditional
status of the reduction stated herein.

All mathematical statements, implications, and reductions remain conditional
exactly as specified in the text.


---

## Integrity note

The existence of this repository is a design choice: the program treats **undischarged assumptions as first‑class objects**. Nothing conditional is hidden, implicit, or informal.

If a statement matters, it is indexed here.
