from sqlalchemy.orm import Session

from . import models, schemas


def get_patients(db: Session):
    return db.query(models.Patient.all())


def get_patient(db: Session, pati_id: str):
    return db.query(models.Patient).filter(models.Patient.Patient_ID == pati_id).first()


def get_acceptance(
    db: Session, acc_id: str, acc_date: str, acc_time: str, pati_id: str
):
    return (
        db.query(models.Acceptance)
        .filter(
            models.Acceptance.Acceptance_ID == acc_id,
            models.Acceptance.Acceptance_Date == acc_date,
            models.Acceptance.Acceptance_Time == acc_time,
            models.Acceptance.Patient_ID == pati_id,
        )
        .first()
    )
