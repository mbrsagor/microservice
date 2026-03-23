from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.endpoints import user, auth

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ScalabixMedical - User Service")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "user_service"}
