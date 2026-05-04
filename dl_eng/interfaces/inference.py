"""Inference contract definitions."""

from abc import ABC, abstractmethod
from typing import Any


class InferenceInterface(ABC):
    """Contract for model execution and sampling."""

    @abstractmethod
    def run(self, inputs: Any) -> Any:
        """Execute inference."""
        pass
