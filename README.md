# Fabrica Runtime

**Fabrica Runtime** is an experimental Python capability interface and Gradio-backed runtime facade in the Fabrica / Digital Fabrica product family.

> Status: **F1 — Fabricated (historical promotion evidence)**. CI run `38161135348` and promotion-commit confirmation run `38629518114` were recorded as successful for F1. The current `main` head contains additional native capability code; its CI result and F2 qualification have **not** been independently reverified in this documentation update. No tagged `v0.1.0-alpha` release is claimed.

## Mission

Build, expose, compose, and operate computational capabilities across human interfaces, APIs, workflows, and agent surfaces while progressively introducing Fabrica-native capability, graph, policy, provenance, and execution semantics.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python examples/hello_fabrica.py
```

Then build applications against the Fabrica namespace:

```python
import fabrica as fab
```

The current alpha facade imports the separately installed `gradio>=6.28,<7` package while adding first-party `PortSpec`, `CapabilitySpec` and `@fab.capability` metadata. These primitives are an initial native semantic layer, not a verified capability graph, security sandbox or F2 operational release.

## Current architecture

```text
Application
   ↓
import fabrica as fab
   ↓
Fabrica public facade
   ↓
Gradio execution/interface substrate
   ↓
UI · API · queue · streaming · workflow · MCP
```

See `ARCHITECTURE.md` for the mutation path toward a Fabrica-native capability and graph kernel.

## Lineage

Fabrica Runtime is a **dependency adapter / facade**, not a demonstrated full-source fork of [gradio-app/gradio](https://github.com/gradio-app/gradio). Gradio is installed as a separate dependency and is licensed under Apache-2.0. The inspected Gradio commit is a source-reference anchor, **not evidence that its source tree was imported**.

Fabrica Runtime is not affiliated with or endorsed by Gradio or Hugging Face. See `UPSTREAM.md` and `NOTICE-DERIVATIVE.md` for attribution and historical provenance; the latter retains its original filename for link continuity.

## Development model

- **GitHub** is authoritative for executable source, history, CI, issues, pull requests, tags, and releases.
- **Google Drive** is authoritative for project intelligence, architecture, provenance, mutation planning, state/handoff, and release records.
- Every mutation follows a **working-first** rule.

## Maturity

- F0 — Seed
- F1 — Fabricated
- F2 — Operational
- F3 — Integrated
- F4 — Native
- F5 — Sovereign

Current target: **F2 — Operational Alpha**.

## License

Apache License 2.0. See `LICENSE`, `UPSTREAM.md`, and `NOTICE-DERIVATIVE.md`.
