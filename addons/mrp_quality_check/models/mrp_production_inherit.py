# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools

class MrpProductionInherit(models.Model):
    _inherit = 'mrp.production'

    def button_mark_done(self):
        sale_lines = self.env['mrp.quality.check'].search([
            ('order_id', '=', self.id),
            ('state','=','pass')
        ])
        if sale_lines: pass
        else:
            return {
                'name': "Quality Control Required",
                'view_mode': 'form',
                'res_model': 'mrp.quality.check',
                'view_id': self.env.ref('mrp_quality_check.mrp_quality_check_warning_form_view').id,
                'type': 'ir.actions.act_window',
                'target': 'new',
            }
        res = super(MrpProductionInherit, self).button_mark_done()
        return res
