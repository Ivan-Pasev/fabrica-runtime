# AGENTS.md — Fabrica Runtime

## Mission
Maintain and evolve Fabrica Runtime as a working public open-source product in the Fabrica / Digital Fabrica portfolio.

## Prime Rule
**WORKING-FIRST.** Every refabrication step must preserve or restore a runnable, testable repository before proceeding.

## Strategy
- Top-down before bottom-up.
- Product identity and portfolio semantics first.
- Preserve compatibility with the mature, separately installed Gradio dependency until a tested Fabrica-native replacement is available.
- Rename public/product surfaces early; rename internal symbols only when justified and tested.
- Prefer adapters and facades before invasive rewrites.
- Keep provenance explicit.
- GitHub is authoritative for executable source.
- Google Drive is authoritative for continuous project intelligence and handoff.

## Lineage
Preserve applicable Apache-2.0 obligations and Gradio attribution. The current package is a dependency adapter/facade, not an authenticated complete Gradio-source import. Do not imply affiliation with Gradio or Hugging Face, or claim third-party code as original Fabrica authorship.

## Maturity
F0 Seed → F1 Fabricated → F2 Operational → F3 Integrated → F4 Native → F5 Sovereign.

## Current Phase
F1 Fabricated is supported by historical CI promotion evidence. The source presently imports `gradio` as a dependency and defines first-party `CapabilitySpec`, `PortSpec`, and `@fab.capability` metadata. **F2 Operational, current-head CI and a tagged alpha release are not verified here.** Do not demand an upstream source-tree import as a prerequisite for the existing dependency-adapter architecture; a future copied-source migration would require a distinct source/rights/history admission gate.
