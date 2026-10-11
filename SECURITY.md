# Security Policy

## Supported versions

During the alpha phase, security fixes target the latest Fabrica Runtime release.

## Reporting

Please use GitHub private vulnerability reporting when available and avoid public disclosure before maintainers have had a reasonable opportunity to investigate and fix the issue.

## Current trust boundary

Fabrica Runtime v0.1 uses Gradio as its initial execution/interface substrate. Application-provided Python callbacks remain trusted application code and are not sandboxed by Fabrica Runtime. Future policy, effect, and sandbox layers must not be assumed before they are implemented and documented.
