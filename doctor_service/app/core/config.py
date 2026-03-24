from pydantic_settings import BaseSettings

# settings class
class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/doctor_db"
    USER_SERVICE_URL: str = "http://localhost:8001"
    
    # We may need the secret key to decode JWT tokens validated by the User Service,
    # or we can rely entirely on calling the user service /me endpoint to validate.
    # Using the /me endpoint is a better microservices pattern.

    class Config:
        env_file = ".env"

settings = Settings()
