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
        with open("foo.png","wb") as f:
            f.write(decodebytes(self.file))
        result = pytesseract.image_to_string(Image.open(r'F:\Downloads\ERP\erp\erp\foo.png'))
        print(result)
        return