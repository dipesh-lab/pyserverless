import pytest
from com.neauron.identity.secrets_client import SecretClient


def test_read_key_returns_none():
    keys = SecretClient(
        "arn:aws:secretsmanager:ap-southeast-2:123456789012:secret:identity"
    )

    assert keys.read_key("test_arn") is None


def test_read_key_returns_none_for_different_arns():
    first = SecretClient(
        "arn:aws:secretsmanager:us-east-1:111111111111:secret:one"
    )
    second = SecretClient(
        "arn:aws:secretsmanager:eu-west-1:222222222222:secret:two"
    )

    assert first.read_key("test_arn") is None
    assert second.read_key("test_arn") is None


def test_read_key_stays_none_across_repeated_calls():
    keys = SecretClient("arn:aws:secretsmanager:us-west-2:999999999999:secret:key")

    assert keys.read_key("test_arn") is None
    assert keys.read_key("test_arn") is None


def test_constructor_requires_arn():
    with pytest.raises(TypeError):
        SecretClient()

