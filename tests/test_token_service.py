import pytest

from com.neauron.identity.token_service import TokenService

@pytest.fixture(autouse=True, scope="function")
def setup_env(monkeypatch):
    monkeypatch.setenv("SECRET_READ_ARN", "arn:aws:secretsmanager:12345")


def test_create_token_returns_empty_string():
    token = TokenService().create_token(3600, ["openid", "profile"])

    assert token == ""


def test_create_token_accepts_empty_scopes():
    token = TokenService().create_token(60, [])

    assert token == ""


def test_create_token_accepts_zero_expiry():
    token = TokenService().create_token(0, ["read"])

    assert token == ""


def test_create_token_returns_a_string():
    token = TokenService().create_token(120, ["write"])

    assert isinstance(token, str)


def test_token_service_can_be_constructed():
    service = TokenService()

    assert isinstance(service, TokenService)
