from typing import List, Optional

from pydantic import BaseModel


class AcceptanceBase(BaseModel):
    Acceptance_Time: str
    Status: int
    Acceptance_Memo: Optional[str] = None


class AcceptanceCreate(AcceptanceBase):
    pass


class Acceptance(AcceptanceBase):
    Acceptance_ID: str
    Acceptance_Date: str
    Patient_ID: str

    class Config:
        orm_mode = True


class PatientBase(BaseModel):
    WholeName: str
    WholeName_inKana: str
    BirthDate: str
    Sex: str


class PatientCreate(PatientBase):
    pass


class Patient(PatientBase):
    Patient_ID: str
    LastVisit_Date: str
    Patient_Memo: str
    Acceptances: List[Acceptance] = []

    class Config:
        orm_mode = True
