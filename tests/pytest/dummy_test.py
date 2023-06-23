

def test_method_is_present() -> None:
    """Confirm that the methods are present."""
    assert "_check_credentials_valid" in dir(ContensisBearer)
    assert "_check_action_allowed" in dir(ContensisBearer)
    assert "_get_action" in dir(ContensisBearer)