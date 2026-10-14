"""Fabrica-native capability metadata and decorator."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from inspect import Parameter, Signature, signature
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def _annotation_name(annotation: Any) -> str:
    if annotation is Signature.empty:
        return "any"
    if annotation is None:
        return "null"
    return getattr(annotation, "__name__", str(annotation))


@dataclass(frozen=True)
class PortSpec:
    name: str
    annotation: str
    required: bool


@dataclass(frozen=True)
class CapabilitySpec:
    id: str
    name: str
    version: str
    inputs: tuple[PortSpec, ...]
    output: str
    effects: tuple[str, ...] = ("PURE",)
    description: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _spec_from_function(
    fn: F,
    *,
    capability_id: str | None,
    version: str,
    effects: tuple[str, ...],
    description: str | None,
) -> CapabilitySpec:
    sig = signature(fn)
    inputs = tuple(
        PortSpec(
            name=name,
            annotation=_annotation_name(param.annotation),
            required=param.default is Parameter.empty,
        )
        for name, param in sig.parameters.items()
    )
    return CapabilitySpec(
        id=capability_id or f"{fn.__module__}.{fn.__qualname__}",
        name=fn.__name__,
        version=version,
        inputs=inputs,
        output=_annotation_name(sig.return_annotation),
        effects=effects,
        description=description or (fn.__doc__.strip() if fn.__doc__ else None),
    )


def capability(
    fn: F | None = None,
    *,
    id: str | None = None,
    version: str = "0.1.0",
    effects: tuple[str, ...] = ("PURE",),
    description: str | None = None,
) -> F | Callable[[F], F]:
    """Declare a Python callable as a Fabrica capability."""

    def decorate(target: F) -> F:
        spec = _spec_from_function(
            target,
            capability_id=id,
            version=version,
            effects=tuple(effects),
            description=description,
        )
        setattr(target, "__fabrica_capability__", spec)
        return target

    if fn is None:
        return decorate
    return decorate(fn)


def get_capability_spec(fn: Callable[..., Any]) -> CapabilitySpec:
    """Return metadata attached to a Fabrica capability."""
    spec = getattr(fn, "__fabrica_capability__", None)
    if not isinstance(spec, CapabilitySpec):
        raise TypeError("object is not a Fabrica capability")
    return spec


def is_capability(fn: Callable[..., Any]) -> bool:
    return isinstance(getattr(fn, "__fabrica_capability__", None), CapabilitySpec)
