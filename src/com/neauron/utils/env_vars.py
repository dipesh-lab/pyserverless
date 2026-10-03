import os

class EnvConfigError(Exception):
    pass


class EnvVars:

    def get_env(self, name: str, def_val: str | None = None) -> str | None:
        return os.environ.get(name, def_val)

    def get_req_env(self, name: str) -> str:
        val = self.get_env(name, None)
        if val is None:
            raise EnvConfigError(f"Required environment configuration '{name}' is missing")
        else:
            return val
