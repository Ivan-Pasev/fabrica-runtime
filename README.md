# Fabrica Runtime

**Fabrica Runtime** is the open-source capability interface and orchestration runtime of the Fabrica / Digital Fabrica product family.

> Status: **F1 candidate**. The Fabrica package surface, smoke tests, CI definition, community files, and local example are now present. Promotion to **F1 — Fabricated** is gated on the first successful GitHub Actions run.

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

The current alpha facade delegates to Gradio internally while keeping the public product surface under Fabrica.

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

Fabrica Runtime is an independent derivative project whose initial implementation substrate is derived from [gradio-app/gradio](https://github.com/gradio-app/gradio), licensed under the Apache License 2.0.

Fabrica Runtime is not affiliated with or endorsed by the Gradio or Hugging Face teams. Upstream attribution and applicable notices are preserved.

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
