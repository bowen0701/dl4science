"""Learning and inference scaffold tests."""

from dl_eng.learners import LearnerState
from dl_eng.inference import SamplingConfig


def test_learner_state_defaults() -> None:
    """Learner state should expose simple training progress fields."""
    state = LearnerState()

    assert state.step == 0
    assert state.epoch == 0


def test_sampling_config_defaults() -> None:
    """Sampling config should expose generation-friendly defaults."""
    config = SamplingConfig()

    assert config.temperature == 1.0
