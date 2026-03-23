from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.endpoints import doctor

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ScalabixMedical - Doctor Service")

app.include_router(doctor.router, prefix="/api/v1/doctors", tags=["doctors"])

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "doctor_service"}
