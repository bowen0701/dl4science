"""Optimization and training loop primitives."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class LearnerState:
    """Mutable training progress state."""

    step: int = 0
    epoch: int = 0
    best_metric: Optional[float] = None
