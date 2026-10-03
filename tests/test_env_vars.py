import os
import pytest

from com.neauron.utils.env_vars import EnvVars, EnvConfigError

def test_var_whenExist_thenEnvValueReturned(monkeypatch):
    monkeypatch.setenv("secret_arn", "arn:aws:secretsmanager:12345")

    val = EnvVars().get_env("secret_arn")

    assert val == "arn:aws:secretsmanager:12345"


def test_var_whenNotExist_thenReturnNone(monkeypatch):
    if "secret_arn" in os.environ:
        del os.environ["secret_arn"]

    val = EnvVars().get_env("secret_arn")

    assert val is None


def test_var_whenNotExist_thenReturnDefaultValue(monkeypatch):
    if "secret_arn" in os.environ:
        del os.environ["secret_arn"]

    val = EnvVars().get_env("secret_arn", "")

    assert val == ""


def test_require_var_whenExist_thenEnvValueReturned(monkeypatch):
    monkeypatch.setenv("secret_arn", "arn:aws:secretsmanager:123456")

    val = EnvVars().get_req_env("secret_arn")

    assert val == "arn:aws:secretsmanager:123456"


def test_required_var_whenNotExist_thenThrowErr():
    if "secret_arn" in os.environ:
        del os.environ["secret_arn"]

    with pytest.raises(EnvConfigError) as exc_info:
        EnvVars().get_req_env("secret_arn")

    assert f"Required environment configuration 'secret_arn' is missing" == str(exc_info.value)