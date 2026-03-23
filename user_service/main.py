from fastapi import FastAPI
from app.db.database import engine, Base
from app.api import user_api, auth_api

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ScalabixMedical - User Service")

app.include_router(auth_api.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(user_api.router, prefix="/api/v1/users", tags=["users"])

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "user_service"}
