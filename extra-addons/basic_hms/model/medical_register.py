from odoo import api, fields, models, _

class Register(models.Model):
    _name = 'medical.register'

    name = fields.Text(string = 'ID')
    status = fields.Text(string = 'status')
    description = fields.Text(string = 'description')
    start = fields.Datetime(string = 'start')
    end = fields.Datetime(string = 'end')

    # def goto_other_view(self):
    #     # 做一些處理或跳轉到其他視圖
    #     # 尚未完成：外部ID無法識別 'my.dialog.my.dialog'SS
    #     action = self.env.ref('medical.register.medical.register').read()[0] 
    #     action['res_id'] = self.id
    #     return action