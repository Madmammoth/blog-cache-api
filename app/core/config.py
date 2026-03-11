from functools import lru_cache

from pydantic import SecretStr, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    postgres_user: str
    postgres_password: SecretStr
    postgres_host: str
    postgres_port: int
    postgres_db: str
    postgres_driver: str = "psycopg"
    postgres_schema: str = "postgresql"

    redis_host: str
    redis_port: int
    redis_db: int
    redis_username: str
    redis_password: SecretStr

    @computed_field
    def dsn(self) -> str:
        url_obj = URL.create(
            drivername=f"{self.postgres_schema}+{self.postgres_driver}",
            username=self.postgres_user,
            password=self.postgres_password.get_secret_value(),
            host=self.postgres_host,
            port=self.postgres_port,
            database=self.postgres_db,
        )

        return url_obj.render_as_string(hide_password=False)


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
