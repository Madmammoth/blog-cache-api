from pydantic import SecretStr, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="POSTGRES_", extra="ignore"
    )

    user: str
    password: SecretStr
    host: str
    port: int
    db: str
    driver: str = "psycopg"
    schema: str = "postgresql"

    @computed_field
    def dsn(self) -> str:
        url_obj = URL.create(
            drivername=f"{self.schema}+{self.driver}",
            username=f"{self.user}",
            password=f"{self.password.get_secret_value()}",
            host=self.host,
            port=self.port,
            database=self.db,
        )
        return url_obj.render_as_string(hide_password=False)
