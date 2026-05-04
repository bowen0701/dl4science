"""Interface import tests."""

from dl_eng.interfaces import (
    DatasetInterface,
    InferenceInterface,
    LearnerInterface,
    ModelInterface,
)


def test_interfaces_are_importable() -> None:
    """Core interfaces should be importable from the package root."""
    assert DatasetInterface is not None
    assert InferenceInterface is not None
    assert LearnerInterface is not None
    assert ModelInterface is not None
