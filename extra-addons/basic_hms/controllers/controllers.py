from odoo import http
from odoo.http import request

class YourController(http.Controller):
    @http.route('/appointment', type='http', auth='public')
    def your_method(self, **kwargs):
        # 解析kwargs並提取需要的參數
        name = kwargs.get('name')
        status = kwargs.get('status')
        start = kwargs.get('start')
        patient_name = kwargs.get('patient_name')
        doctor_name = kwargs.get('doctor_name')
        # 建立新的Register記錄並將數據填入
        register = http.request.env['medical.register'].sudo().create({
            'name': name,
            'status': status,
            'start': start,
            'patient_name': patient_name,
            'doctor_name': doctor_name
        })
        return "<h1>預約成功</h1>"