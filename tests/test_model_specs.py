"""Model scaffold tests."""

from dl_eng.models import DiffusionModelSpec, TransformerModelSpec


def test_transformer_model_spec_defaults() -> None:
    """Transformer defaults should be populated."""
    spec = TransformerModelSpec()

    assert spec.d_model > 0
    assert spec.n_layers > 0


def test_diffusion_model_spec_defaults() -> None:
    """Diffusion defaults should be populated."""
    spec = DiffusionModelSpec()

    assert spec.timesteps > 0
    assert spec.prediction_target == "epsilon"
