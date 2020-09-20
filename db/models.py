from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Patient(Base):
    __tablename__ = "patient"

    Patient_ID = Column(String, primary_key=True, index=True)
    WholeName = Column(String, index=True)
    WholeName_inKana = Column(String, index=True)
    BirthDate = Column(String)
    Sex = Column(String)
    LastVisit_Date = Column(String)
    Patient_Memo = Column(String)

    Acceptances = relationship("Acceptance", back_populates="Patient")


class Acceptance(Base):
    __tablename__ = "acceptance"

    Acceptance_ID = Column(String, primary_key=True)
    Acceptance_Date = Column(String, primary_key=True)
    Acceptance_Time = Column(String)
    Status = Column(Integer)
    Patient_ID = Column(String, ForeignKey("patient.Patient_ID"))
    Acceptance_Memo = Column(String)

    Patient = relationship("Patient", back_populates="Acceptances")
