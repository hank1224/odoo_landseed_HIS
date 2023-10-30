import json
import requests

def convert_to_fhir(data):
    fhir_data = {
        "resourceType": "Practitioner",
        "identifier": [
            {
                "value": data["identifier"]
            }
        ],
        "name": [
            {
                "family": data["lastName"],
                "given": data["firstName"]
            }
        ],
        "gender": data["gender"],
        "birthDate": data["birthDate"],
        "address": [
            {
                "use": "home",
                "line": data["addressLine"],
                "city": data["city"],
                "state": data["state"],
                "postalCode": data["postalCode"]
            }
        ],
        "telecom": [
            {
                "system": "phone",
                "value": data["phone"]
            },
            {
                "system": "email",
                "value": data["email"]
            }
        ],
        "qualification": [
            {
                "identifier": [
                    {
                        "value": data["qualificationIdentifier"]
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v2-0360",
                            "code": data["qualificationCode"],
                            "display": data["qualificationDisplay"]
                        }
                    ]
                },
                "period": {
                    "start": data["qualificationStartDate"],
                    "end": data["qualificationEndDate"]
                }
            }
        ]
    }
    return fhir_data

def send_fhir_data(fhir_data):
    url = "http://localhost:8080/fhir/Practitioner"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(fhir_data))
    if response.status_code == 201:
        print("資料成功傳送！")
    else:
        print("資料傳送失敗。錯誤碼：", response.status_code)

# 假設表單有以下欄位
form_data = {
    "identifier": "DOC1",
    "firstName": "1",
    "lastName": "醫生",
    "gender": "male",
    "birthDate": "1980-04-26",
    "addressLine": "竹北豪宅豪宅",
    "city": "Hsinchu",
    "state": "竹北",
    "postalCode": "10001",
    "phone": "1234567890",
    "email": "johndoe@example.com",
    "qualificationIdentifier": "Q12345",
    "qualificationCode": "MD",
    "qualificationDisplay": "Doctor of Medicine",
    "qualificationStartDate": "2000-01-01",
    "qualificationEndDate": "2045-12-31"
}

fhir_data = convert_to_fhir(form_data)
send_fhir_data(fhir_data)
print(json.dumps(fhir_data, indent=4))