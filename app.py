from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AccDate(BaseModel):
    acceptance_date: str


@app.post("/api/acceptances")
async def acceptances(data: AccDate):
    print(data)
    # return {"text": f"hello world, {data.acceptance_date}"}
    date = data.acceptance_date
    # Acceptance.check(selected_date=date)
    acceptances = Acceptance.get_list(selected_date=date)
    acceptance_schema = AcceptanceSchema()
    patient_schema = PatientSchema()
    data = []
    for acc in acceptances:
        d1 = acceptance_schema.dump(acc[0])
        d2 = patient_schema.dump(acc[1])
        d1["WholeName_inKana"] = d2["WholeName_inKana"]
        d1["WholeName"] = d2["WholeName"]
        d1["BirthDate"] = calc_age(d2["BirthDate"])
        d1["Sex"] = "男" if d2["Sex"] == "1" else "女"
        d1["LastVisit_Date"] = d2["LastVisit_Date"]
        d1["Patient_Memo"] = d2["Patient_Memo"]
        data.append(d1)

    return make_response(jsonify(data))
