"""Fabrica Runtime public facade."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

import gradio as _gradio
from gradio import *  # noqa: F401,F403

try:
    __version__ = version("fabrica-runtime")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.1.0a0"

UPSTREAM_RUNTIME = "gradio"


def upstream_version() -> str:
    """Return the active Gradio substrate version."""
    return getattr(_gradio, "__version__", "unknown")

from .capability import CapabilitySpec, PortSpec, capability, get_capability_spec, is_capability
