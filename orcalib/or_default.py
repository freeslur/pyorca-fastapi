default_url = "http://trial.orca.med.or.jp:8000"
patient_info = "/api01rv2/patientgetv2?"
acceptance_cancel = "/orca11/acceptmodv2"
regist_receipt = "/api21/medicalmodv2?class=01"
post_headers = {"Content-Type": "application/xml"}
auth = ("trial", "")
# auth = ("ormaster", "ormaster")


def acceptance_all(class_num):
    return "/api01rv2/acceptlstv2?class=0" + str(class_num)
