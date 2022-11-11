# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from typing_extensions import Required
from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools import formataddr
from datetime import datetime

from base64 import decodebytes
from PIL import Image
import re
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' #Win

# import requests

# model_id = '85638d0d-c529-4d6c-887e-0abf0860d36c'
# api_key = '-7KFB559oxL207NerveYa6NX-Gk-YiJ9'

# url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/LabelFile/'

# print(url)

# data = {'file': open(r'/Users/William/Downloads/odoo16/erp/foo.png', 'rb'),    'modelId': ('', model_id)}

# response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)

# print(response.text)

class SaleOrderOcr(models.TransientModel):
    _name = 'sale.order.ocr'
    _description = "Sales Order OCR"

    file = fields.Binary(string ="Image")   

    def action_get_text(self):
        self.ensure_one()
        with open("foo.png","wb") as f:
            f.write(decodebytes(self.file))
        text = pytesseract.image_to_string(Image.open(r'F:\Downloads\ERP\erp\erp\foo.png')) #Win
        #text = pytesseract.image_to_string(Image.open(r'/Users/William/Downloads/odoo16/erp/foo.png'))#Mac

        text_after_split = list(filter(None, text.split('\n')))
        customer = ''
        productsIndex = 0
        quantityIndex = 0
        unitPriceIndex = 0
        taxesIndex = 0

        for i in range(len(text_after_split)):
            if ('Address' in text_after_split[i]): customer = text_after_split[i+1]
            if ('Products' in text_after_split[i] or 'Description' in text_after_split[i]): productsIndex = i
            if ('Quantity' in text_after_split[i]): quantityIndex = i
            if ('Unit Price' in text_after_split[i]): unitPriceIndex = i
            if ('Tax' in text_after_split[i]): taxesIndex = i

        customer = customer.split(',')[0]

        product = []
        for i in text_after_split[productsIndex+1:quantityIndex]:
            m = re.search('\[(.+?)\]', i)
            if m: 
                product.append(m.group(1))

        quantity = []
        for i in text_after_split[quantityIndex+1:unitPriceIndex]:
            quantity.append(i.split(' ')[0])

        unitPrice = []
        for i in text_after_split[unitPriceIndex+1:taxesIndex]:
            unitPrice.append(i.split(' ')[0])

        partner = self.env['res.partner'].search([('name', '=', customer)])

        # pricelist_days = 'Public Pricelist'
        # pricelist = self.env['product.pricelist'].search([('name', '=', pricelist_days)])

        # payment_term = 'End of Following Month'
        # payment = self.env['account.payment.term'].search([('name', '=', payment_term)])

        sale_id = self.env['sale.order'].create(    
            {'partner_id': partner.id,      
            'date_order': datetime.now(),
            #'pricelist_id': pricelist.id,
            #'payment_term_id': payment.id,  
        })

        for i in range(len(product)):
            p = self.env['product.product'].search([('default_code', '=', product[i])])
            if p.id:
                self.env['sale.order.line'].create({
                    'product_id': p.id,
                    'order_id': sale_id.id,
                    'product_uom_qty' : quantity[i], 
                    'price_unit': unitPrice[i],
                })   

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'sale.order',
            'views': [(self.env.ref("sale.view_order_form").id, 'form')],
            'res_id': sale_id.id,
            'target': 'current',
        }