# Upstream Lineage

Fabrica Runtime builds a distinct Python capability facade around the separately installed, Apache-2.0 licensed **Gradio** project.

- Upstream repository: https://github.com/gradio-app/gradio
- Initial inspected upstream reference commit (not an imported-source baseline): `526c24340024dfae9c9a7709aad552382ed99f86`
- Upstream license: Apache License 2.0

## Current source relationship: dependency adapter

The current package declares `gradio>=6.28,<7` as a runtime dependency and imports/re-exports its public Python interfaces. No complete copied Gradio source tree has been established in the inspected Fabrica Runtime repository. The pinned upstream reference documents research/provenance, **not Git import lineage**.

Preserve applicable upstream copyright, patent, trademark, and attribution obligations and all pre-existing notices. Fabrica claims authorship only over its original facade, capability primitives, documentation, integrations and future code. A future copied-source refabrication must pass a separate license and acquisition-history gate before that relationship is asserted.

Fabrica Runtime is an independent project and is not affiliated with or endorsed by Gradio or Hugging Face.
