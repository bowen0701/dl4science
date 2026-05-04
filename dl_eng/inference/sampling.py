"""Sampling configurations and orchestrators."""

from dataclasses import dataclass


@dataclass(frozen=True)
class SamplingConfig:
    """Hyperparameters for sequence or image generation."""

    temperature: float = 1.0
    top_p: float = 1.0
    max_new_tokens: int = 128
    do_sample: bool = False
