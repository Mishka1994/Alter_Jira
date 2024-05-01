from pydantic import Field
from pydantic_settings import BaseSettings


class DataBaseSettings(BaseSettings):
    host: str = Field('localhost', env='POSTGRES_HOST')
    port: int = Field(5432, env='POSTGRES_PORT')
    username: str = Field('postgres', env='POSTGRES_USER')
    password: str = Field('postgres', env='POSTGRES_PASSWORD')
    database: str = Field('postgres', env='POSTGRES_DB')

    @property
    def uri(self):
        return f'postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}'


class AppSettings(BaseSettings):
    db: DataBaseSettings = DataBaseSettings()
    title: str = 'Alter_Jira'
    version: str = '0.1.0'
