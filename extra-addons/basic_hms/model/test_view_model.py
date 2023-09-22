from odoo import api, fields, models, _

class Dialog(models.Model):
    _name = 'my.dialog'

    name = fields.Text(string='Message')

    def goto_other_view(self):
        # 做一些處理或跳轉到其他視圖
        # 尚未完成：外部ID無法識別 'my.dialog.my.dialog'SS
        action = self.env.ref('my.dialog.my.dialog').read()[0] 
        action['res_id'] = self.id
        return action