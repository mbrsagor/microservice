from sqlalchemy.orm import Session
from app.models.model import Doctor
from app.schemas.doctor_schema import DoctorCreate, DoctorUpdate


class DoctorRepository:

    # get all doctors
    def get_all(self, db: Session):
        return db.query(Doctor).all()

    # get doctor by id
    def get(self, db: Session, doctor_id: int):
        return db.query(Doctor).filter(Doctor.id == doctor_id).first()

    # get doctor by user id
    def get_by_user_id(self, db: Session, user_id: int):
        return db.query(Doctor).filter(Doctor.user_id == user_id).first()

    # create doctor
    def create(self, db: Session, obj_in: DoctorCreate):
        db_obj = Doctor(
            user_id=obj_in.user_id,
            specialization=obj_in.specialization,
            experience_years=obj_in.experience_years,
            is_available=obj_in.is_available
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    # update doctor
    def update(self, db: Session, db_obj: Doctor, obj_in: DoctorUpdate):
        db_obj.specialization = obj_in.specialization
        db_obj.experience_years = obj_in.experience_years
        db_obj.is_available = obj_in.is_available
        db.commit()
        db.refresh(db_obj)
        return db_obj

doctor_repository = DoctorRepository()
