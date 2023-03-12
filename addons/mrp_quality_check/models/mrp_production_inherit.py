# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools
from odoo.exceptions import UserError

class MrpProductionInherit(models.Model):
    _inherit = 'mrp.production'

    def button_mark_done(self):
        sale_lines = self.env['mrp.quality.check'].search([
            ('order_id', '=', self.id),
            ('state','=','pass')
        ])
        if sale_lines: pass
        else:
            raise UserError('Please check the Quality Control for this order first')
        res = super(MrpProductionInherit, self).button_mark_done()
        return res
