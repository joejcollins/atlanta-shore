"""Confirm that the settings module is working as expected."""
from python_src.settings import ATLANTA_SHORE


def test_settings() -> None:
    """Test that the static settings are correct."""
    # ASSERT
    assert ATLANTA_SHORE.log_level == "WARN"
    assert ATLANTA_SHORE.observations_files[0].startswith("./data/raw/")
