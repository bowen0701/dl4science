"""Batch-level data containers."""

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class BatchSpec:
    """Lightweight structured batch container."""

    inputs: Any
    targets: Optional[Any] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
