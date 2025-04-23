import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv



# Загружаем переменные окружения ДО инициализации настроек
load_dotenv(
    dotenv_path=os.path.join(os.path.dirname(__file__), ".", ".env")
)

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_PASSWORD: str
    DB_NAME: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"  # Добавляем значение по умолчанию
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    API_KEY: str
    FOLDER_ID: str
    ADMIN_MAIL: str
    MAIL_PORT: int

    @property
    def DATABASE_URL(self) -> str:
        return f"mysql://{self.DB_NAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}"

    @property
    def ASYNC_DATABASE_URL(self) -> str:
        return f"mysql+asyncmy://{self.DB_NAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}"


#extra - игнорирование других переменных
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()

def get_auth_data():
    return {'secret_key': settings.SECRET_KEY, 'algorithm': settings.ALGORITHM}

def get_admin_mail():
    pass

