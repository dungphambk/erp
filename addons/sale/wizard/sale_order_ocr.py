# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from typing_extensions import Required
from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools import formataddr

from base64 import decodebytes
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

class SaleOrderOcr(models.TransientModel):
    _name = 'sale.order.ocr'
    _description = "Sales Order OCR"

    file = fields.Binary(string ="Image")

    def action_get_text(self):
        self.ensure_one()
        with open("foo.png","wb") as f:
            f.write(decodebytes(self.file))
        text = pytesseract.image_to_string(Image.open(r'F:\Downloads\ERP\erp\erp\foo.png'))
        print(text)

        # template_id = self.env['ir.model.data']._xmlid_to_res_id(
        #     'sale.mail_template_sale_cancellation', raise_if_not_found=False
        # )
        # lang = self.env.context.get('lang')
        # template = self.env['mail.template'].browse(template_id)
        # if template.lang:
        #     lang = template._render_lang(self.ids)[self.id]
        # ctx = {
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_order_id': self.id,
        #     'mark_so_as_canceled': True,
        #     'default_email_layout_xmlid': "mail.mail_notification_layout_with_responsible_signature",
        # }
        ctx = {
            'default_partner_id': 'Deco Addict',
            'default_date_order': '2022-11-02',
        }
        try:
            form_view_id = self.env.ref("sale.view_order_form").id
        except Exception as e:
            form_view_id = False
        return {
            'type': 'ir.actions.act_window',
            'name': 'Test',
            'view_mode': 'form',
            'res_model': 'sale.order',
            'views': [(form_view_id, 'form')],
            'target': 'current',
            'context': ctx,
        }