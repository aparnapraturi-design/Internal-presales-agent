#  InternalAgent – Structured AI Document Generation System

InternalAgent is a AI system for generating, refining, and managing long-form business documents (Feasibility Reports, Technical Scopes, Commercial Proposals) from messy inputs such as discovery calls, transcripts, and human edits.

It is a **stateful document intelligence pipeline** designed to behave predictably under regeneration, refinement, and human-in-the-loop workflows.

---

## ✨ Key Capabilities

- 🧾 Generate report sections **one at a time**
- ✏️ Refine existing sections faithfully (instruction-first)
- 🔄 Sync human-edited sections from DB on every generate call
- 📚 Extract and reuse facts from transcripts
- 🔁 Regenerate sections without re-interpreting raw calls
- 👤 Treat human edits as authoritative
- 🧠 Ready for Knowledge Base / RAG integration
- 🔍 Fully traceable and debuggable

---

## 🧠 Core Design Philosophy

InternalAgent separates:
- **Understanding** (transcripts → facts)
- **Writing** (facts → sections)
- **Editing** (human instruction → refinement)

This prevents silent hallucination, constraint loss, and cross-section drift.

---

## 🏗️ High-Level Architecture

```
1. Client API Call (Generate)
      │
      ▼
SessionState Graph (LangGraph)
      │
      ├─► Load Transcripts (cached)
      │
      ├─► Extract Context & Facts (cached)
      │
      ├─► Sync Sections from DB (human edits)
      │
      ▼
Standalone Program
  - generate_section
      │
      ▼
Persist Section + Update SessionState
                                          
---

2. Client API Call (Refine)
      │
      ▼
Load Existing SessionState (no mutation)
      │
      ▼
Standalone Program
  - refine_section
      │
      ▼
Overwrite Section Content 
---


## 🔄 Execution Flow

### 1️⃣ Build Session Graph (Every GENERATE Call)
A fresh LangGraph session graph is created for every API generate call to ensure:
- no stale state
- latest DB edits are respected
- idempotent behavior

LangGraph is used **only for orchestration**, not for writing sections.

---


### 2️⃣  Load Transcripts (Once per Session)

- Files fetched from storage / DB
- Transcripts extracted and cached locally
- - Transcripts are treated as **immutable within a single session**


---

### 3️⃣Context & Fact Extraction (Once per Session)

- Transcripts are chunked
- Atomic facts extracted with evidence
- Facts stored as JSON on disk
- SessionState stores only file references

---

### 4️⃣ Sync Sections from DB (Every Generate Call)

- Query DB for sections belonging to `(customer_id, opportunity_id, report_type)`
- Compare DB timestamps with cached metadata
- Fetch **only modified sections**
- Cache locally and update `SessionState.completed_sections`

DB is the **source of truth**.

---

### 5️⃣ Section Generation (Standalone)

`generate_section`:
- consumes prepared SessionState
- reads extracted facts
- applies section intent
- writes text section to disk
- updates `completed_sections`

---

### 6️⃣ Section Refinement (Standalone)

`refine_section`:
- treats original section as authoritative
- follows user instruction strictly
- uses facts only if requested


Refinement never regenerates.

---

## 📦 Repository Structure

src/
├── core/
│   ├── nodes/                        # LangGraph nodes (state orchestration only)
│   │   ├── transcript_loader_node.py
│   │   ├── context_extractor_node.py
│   │   ├── section_sync_node.py
│   │   └── config.py                 # hydrate_from_config
│   │
│   ├── programs/                    # Standalone business logic (NOT graph nodes)
│   │   ├── generate_section.py
│   │   └── refine_section.py
│   │
│   ├── schemas/                     # Pydantic contracts
│   │   ├── fact_schema.py
│   │   ├── reports_schema.py
│   │   └── state_schema.py
│   │
│   ├── tools/                       # Low-level reusable utilities
│   │   ├── llm.py                   # generate_text / generate_json
│   │   ├── chunking.py              # text chunking logic
│   │   ├── transcript_extractor.py  # pdf/audio/doc → text
│   │   └── storage.py               # file IO / temp helpers (if present)
│   │
│   ├── state.py                     # SessionState, FileRef, SectionRef (imported widely)
│   │
│   └── utils/                       # Pure helpers (no side effects)
│       └── hashing.py / text.py     # (if present)
│
├── api/
│   ├── main.py                      # FastAPI entrypoint
│   └── constants.py                 # headers, error codes, status enums
│
├── .temp/                           # Runtime artifacts (gitignored)
│   ├── transcripts/
│   ├── context/
│   └── sections/
│
├── trial_graph.py                   # Local LangGraph runner / debugging
├── README.md
└── pyproject.toml / requirements.txt


---

## ✍️ Generate vs Refine vs Sync

| Action | Purpose | Authority |
|------|--------|-----------|
| Sync | Load DB edits | Human |
| Generate | Create new section | Facts |
| Refine | Edit section | User |

> **Generate creates truth.  
> Refine edits truth.  
> Sync preserves truth.**

---

## 🚀 Future Extensions

- 🔍 Knowledge Base / RAG integration
- 📊 Section-level QA agents
- 🔄 DB conflict detection
- 📈 Streaming generation

---


