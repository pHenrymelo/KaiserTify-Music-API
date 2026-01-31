from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  db_host: str
  db_port: int
  db_name: str
  db_user: str
  db_password: str

  secret_key: str

  @property
  def database_url(self) -> str:
    return (
      f"postgresql+psycopg2://"
      f"{self.db_user}:{self.db_password}"
      f"@{self.db_host}:{self.db_port}/{self.db_name}"
    )

  class Config:
    env_file = ".env"

settings = Settings()