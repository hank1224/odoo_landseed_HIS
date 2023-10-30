import json
import requests

def convert_to_fhir(data):
    # 表單資料轉換為FHIR資源的程式碼
    fhir_data = {
        "resourceType": "Appointment",
        "identifier": [
            {
                "value": data["identifier"],
            }
        ],
        "status": "booked",
        "start": data["start"],
        "end": data["end"],
        "participant": [
            {
                "actor": {
                    "reference": data["patientReference"]
                },
                "status": "accepted"
            },
            {
                "actor": {
                    "reference": data["doctorReference"]
                },
                "status": "accepted"
            }
        ]
    }
    return fhir_data


def send_fhir_data(fhir_data):
    url = "http://localhost:8080/fhir/Appointment"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(fhir_data))
    if response.status_code == 201:
        print("資料成功傳送！")
    else:
        print("資料傳送失敗。錯誤碼：", response.status_code)

# 假設表單有以下欄位
form_data = {
    "identifier": "appointment1",
    "start": "2023-11-04T10:30:00Z",
    "end": "2023-11-04T11:30:00Z",
    "patientReference": "Patient?identifier=PAC1", 
    "doctorReference": "Practitioner?identifier=DOC1",
}

fhir_data = convert_to_fhir(form_data)
send_fhir_data(fhir_data)
print(json.dumps(fhir_data, indent=4))