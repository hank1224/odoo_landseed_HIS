from odoo import api, fields, models, http, _
import json
import requests
from odoo.http import request

class Register(models.Model):
    _name = 'medical.register'

    name = fields.Text(string = '預約號碼')
    status = fields.Text(string = '狀態')
    section = fields.Text(str = '科別')
    description = fields.Text(string = '描述')
    start = fields.Datetime(string = '掛號時間')
    end = fields.Datetime(string = '結束時間')
    patient_id = fields.Many2one('medical.patient','病患名稱')
    doctor_id = fields.Many2one('medical.physician','醫師名稱')

    def goto_other_view(self):
        form_data = {
            "identifier": self.name,
            "description": self.description,
            "start": self.start.strftime('%Y-%m-%dT%H:%M:%SZ'),
            "end": self.end.strftime('%Y-%m-%dT%H:%M:%SZ'),
            "patientReference": "Patient?identifier="+self.patient_id.name,
            "doctorReference": "Practitioner?identifier="+self.doctor_id.code,
        }
        print(form_data)
        fhir_data = convert_to_fhir(form_data)
        # 傳送FHIR格式的資料
        send_fhir_data(fhir_data)

    def import_fhir_data(self):
        url = "http://localhost:8080/fhir/Appointment"  # FHIR API的URL
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            fhir_data = response.json()
            entries = fhir_data.get('entry', [])
            for entry in entries:
                resource = entry.get('resource', {})
                patient_name = resource.get('participant', [{}])[0].get('actor', {}).get('reference', '')
                doc_name = resource.get('participant', [{}])[1].get('actor', {}).get('reference', '')
                response2 = requests.get('http://localhost:8080/fhir/'+patient_name)
                response3 = requests.get('http://localhost:8080/fhir/'+doc_name)
                patient_data = response2.json()
                doc_data = response3.json()
                # 取得Patient的name
                patient_name2 = patient_data.get('identifier', [{}])[0].get('value', [''])
                doc_name2 = doc_data.get('identifier', [{}])[0].get('value', [''])
                print(patient_name2)
                print(doc_name2)
                patient = self.env['medical.patient'].search([('name', '=', patient_name2)], limit=1)
                doctor = self.env['medical.physician'].search([('code', '=', doc_name2)], limit=1)
                appointment_name = resource.get('identifier', [{}])[0].get('value', '')
                appointment_data = {
                    'name': appointment_name,
                    'status': resource.get('status', ''),
                    'description': resource.get('description', ''),
                    'start': resource.get('start', '').replace('T', ' ').replace('Z', ''),
                    'end': resource.get('end', '').replace('T', ' ').replace('Z', ''),
                    'patient_id': patient.id,
                    'doctor_id': doctor.id
                }
                print(appointment_data)
                self.create(appointment_data)
            return {'success': True, 'message': 'FHIR data imported successfully'}
        else:
            return {'success': False, 'message': 'Failed to fetch FHIR data'}

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
        "description": data["description"],
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
    # 將FHIR格式的資料傳送出去
    # 替換成實際的FHIR服務端點URL
    # 參考https://hapi.fhir.org/
    url = "http://localhost:8080/fhir/Appointment" # 測試用伺服器
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(fhir_data, default=str))
    if response.status_code == 201:
        print("資料成功傳送！")
    else:
        print("資料傳送失敗。錯誤碼：", response.status_code)
        print("錯誤原因：", response.text)