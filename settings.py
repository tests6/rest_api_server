from pydantic import BaseSettings


class Settings(BaseSettings):
    db_protocol: str
    db_username: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str

    class Config:
        env_file = ".env"
