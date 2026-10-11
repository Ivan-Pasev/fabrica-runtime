# Fabrica Runtime Architecture

## Current stage

Fabrica Runtime currently exposes a Fabrica public namespace over the mature Gradio runtime substrate.

Application -> Fabrica facade -> Gradio substrate -> UI / API / queue / streaming / workflow / MCP.

This outside-in structure is intentional: product identity and public semantics advance before deep internal replacement.

## Target architecture

Canonical Capability IR -> Law / Authority / Effects / Provenance -> Execution Graph -> Projection Compiler -> UI / API / MCP / CLI / Skill / Canvas.

## Core invariant

No architectural mutation should intentionally leave the default branch non-installable or non-runnable.
