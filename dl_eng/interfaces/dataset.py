"""Dataset contract definitions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable


class DatasetInterface(ABC):
    """Contract for dataset providers."""

    @abstractmethod
    def __len__(self) -> int:
        """Return dataset size."""
        pass

    @abstractmethod
    def iter_batches(self) -> Iterable[Any]:
        """Yield batches for training or evaluation."""
        pass
