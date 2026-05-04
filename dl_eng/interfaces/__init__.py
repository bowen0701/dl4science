"""Abstract contracts for dl-eng subsystems."""

from dl_eng.interfaces.dataset import DatasetInterface
from dl_eng.interfaces.inference import InferenceInterface
from dl_eng.interfaces.learner import LearnerInterface
from dl_eng.interfaces.model import ModelInterface

__all__ = [
    "DatasetInterface",
    "InferenceInterface",
    "LearnerInterface",
    "ModelInterface",
]
