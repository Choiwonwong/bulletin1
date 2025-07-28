from typing import Literal

from pydantic import Field as PydanticField
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    pool_size: int = 5
    max_overflow: int = 10
    pool_timeout: int = 30
    pool_recycle: int = 3600  # 1시간 (3600초)


class MySQLSettings(DatabaseSettings):
    model_config = SettingsConfigDict(env_prefix="MYSQL_")
    host: str = "localhost"
    port: int = 3306
    user: str
    password: str
    database: str = "bulletin1"
    charset: str = "utf8mb4"  # MySQL 특정 설정

    @property
    def database_url(self) -> str:
        return f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}?charset={self.charset}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_nested_delimiter="_", case_sensitive=False
    )

    app_env: Literal["local", "production"] = "local"
    db_type: Literal["mysql"] = "mysql"

    mysql: MySQLSettings = PydanticField(default_factory=MySQLSettings)

    @property
    def database_url(self) -> str:
        if self.db_type == "mysql" and self.mysql:
            return self.mysql.database_url
        else:
            raise ValueError(f"Unsupported database type: {self.db_type}")

    @property
    def current_db_settings(self) -> DatabaseSettings:
        if self.db_type == "mysql" and self.mysql:
            return self.mysql
        else:
            raise ValueError(f"Unsupported database type: {self.db_type}")


settings = Settings()
