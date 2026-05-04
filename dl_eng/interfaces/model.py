"""Model contract definitions."""

from abc import ABC, abstractmethod
from typing import Any


class ModelInterface(ABC):
    """Contract for trainable model components."""

    @abstractmethod
    def forward(self, batch: Any) -> Any:
        """Run a forward pass."""
        pass

    @abstractmethod
    def loss(self, batch: Any) -> Any:
        """Compute the training loss for a batch."""
        pass
