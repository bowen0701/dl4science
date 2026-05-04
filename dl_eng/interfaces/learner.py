"""Learner contract definitions."""

from abc import ABC, abstractmethod
from typing import Any


class LearnerInterface(ABC):
    """Contract for optimization logic."""

    @abstractmethod
    def train_step(self, batch: Any) -> Any:
        """Run one optimization step."""
        pass

    @abstractmethod
    def fit(self) -> Any:
        """Run the configured learning procedure."""
        pass
