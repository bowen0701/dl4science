"""Diffusion-oriented model definitions."""

from dataclasses import dataclass


@dataclass
class DiffusionModelSpec:
    """Configuration stub for diffusion family models."""

    input_channels: int = 4
    model_channels: int = 256
    timesteps: int = 1000
    prediction_target: str = "epsilon"
