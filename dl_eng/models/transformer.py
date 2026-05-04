"""Transformer-oriented model definitions."""

from dataclasses import dataclass


@dataclass
class TransformerModelSpec:
    """Configuration stub for transformer family models."""

    d_model: int = 768
    n_layers: int = 12
    n_heads: int = 12
    vocab_size: int = 50257
    context_length: int = 1024
