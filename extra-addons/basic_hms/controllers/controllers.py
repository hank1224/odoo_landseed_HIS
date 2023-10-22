from odoo import http

class YourController(http.Controller):
    @http.route('/post', type='http', auth='public')
    def your_method(self, **kwargs):
        # 解析kwargs並提取需要的參數
        name = kwargs.get('name')
        status = kwargs.get('status')
        description = kwargs.get('description')
        start = kwargs.get('start')
        end = kwargs.get('end')
        patient_id = kwargs.get('patient_id')
        doctor_id = kwargs.get('doctor_id')
        # 建立新的Register記錄並將數據填入
        # sudo -> super user
        register = http.request.env['medical.register'].sudo().create({
            'name': name,
            'status': status,
            'description': description,
            'start': start,
            'end': end,
            'patient_id': patient_id,
            'doctor_id': doctor_id
        })
        return "預約成功"