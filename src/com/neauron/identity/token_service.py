from com.neauron.identity.secrets_client import SecretClient
from com.neauron.utils.env_vars import EnvVars

class TokenService:

    _secret_client: SecretClient
    _env_vars : EnvVars

    def __init__(self):
        _env_vars = EnvVars()
        _secret_client = SecretClient(_env_vars.get_req_env("SECRET_READ_ARN"))


    def create_token(self, exp_seconds: int, scopes: list[str]):
        return ""

