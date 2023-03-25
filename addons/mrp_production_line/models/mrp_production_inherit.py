# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools
from odoo.exceptions import UserError

class MrpProductionInherit(models.Model):
    _inherit = 'mrp.production'

    # production_line = fields.Many2one('mrp.production.line', string="Production Line", domain="[('state','=', 'available')]")

    def button_mark_done(self):
        log = self.env['mrp.production.log'].search([
            ('order_id', '=', self.id),
            ('state','=','done'),
        ])
        if log: pass
        else:
            raise UserError('This order has not been produced')
        res = super(MrpProductionInherit, self).button_mark_done()
        return res
