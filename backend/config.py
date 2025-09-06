from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    database_url: str = Field(validation_alias="DATABASE_URL")
    db_user: str = Field(validation_alias="DB_USER")
    db_password: str = Field(validation_alias="DB_PASSWORD")
    
    # Authentication settings
    secret_key: str = Field(default="your-secret-key-change-this-in-production")
    algorithm: str = Field(default="HS256")
    access_token_expire_minutes: int = Field(default=30)
    
    # Admin credentials (change these!)
    admin_username: str = Field(default="admin")
    admin_password: str = Field(default="admin123")  # This should be hashed in production

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
