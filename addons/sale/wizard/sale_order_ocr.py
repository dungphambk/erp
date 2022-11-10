# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from typing_extensions import Required
from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools import formataddr

from base64 import decodebytes
from PIL import Image
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' #Win/Mac

class SaleOrderOcr(models.TransientModel):
    _name = 'sale.order.ocr'
    _description = "Sales Order OCR"

    file = fields.Binary(string ="Image")

    def action_get_text(self):
        self.ensure_one()
        with open("foo.png","wb") as f:
            f.write(decodebytes(self.file))
        #text = pytesseract.image_to_string(Image.open(r'F:\Downloads\ERP\erp\erp\foo.png')) #Win/Mac
        text = pytesseract.image_to_string(Image.open(r'/Users/William/Downloads/odoo16/erp/foo.png'))
        
        print(text)

        name = 'Deco Addict'
        partner = self.env['res.partner'].search([('name', '=', name)])

        pricelist_days = 'Public Pricelist'
        pricelist = self.env['product.pricelist'].search([('name', '=', pricelist_days)])

        payment_term = 'End of Following Month'
        payment = self.env['account.payment.term'].search([('name', '=', payment_term)])

        sale_id = self.env['sale.order'].create(    
            {'partner_id': partner.id,      
            'date_order': '2022-11-02',
            'validity_date': '2022-11-04',
            'pricelist_id': pricelist.id,
            'payment_term_id': payment.id,  
        })

        product_code = ['E-COM06', 'E-COM07']
        product_qty = [2,3]
        #product_price = [100,200]
        for i in range(len(product_code)):
            product = self.env['product.product'].search([('default_code', '=', product_code[i])])
            if product.id:
                self.env['sale.order.line'].create({
                    'product_id': product.id,
                    'order_id': sale_id.id,
                    'product_uom_qty' : product_qty[i], 
                    #'price_unit': product_price[i],
                })   

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'sale.order',
            'views': [(self.env.ref("sale.view_order_form").id, 'form')],
            'res_id': sale_id.id,
            'target': 'current',
        }