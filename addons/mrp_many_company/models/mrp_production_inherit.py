# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class MrpProductionInherit(models.Model):
    _inherit = 'mrp.production'

    is_our_company = fields.Boolean(string='Is Our Company', compute='_compute_is_our_company')

    @api.depends_context('uid')
    def _compute_is_our_company(self):
        user_company_id = self.env.user.company_id.id
        dev_list = self.env['mrp.develop'].search([])
        for rec in dev_list:
            if (rec.company_id):
                if rec.company_id.id != user_company_id:
                    rec.related_field = False
                else:
                    rec.related_field = True
        
        line = self.env['mrp.production.line'].search([])
        for rec in line:
            if rec.company_id.id != user_company_id:
                rec.related_field = False
            else:
                rec.related_field = True
        
        log = self.env['mrp.production.log'].search([])
        for rec in log:
            if rec.company_id.id != user_company_id:
                rec.related_field = False
            else:
                rec.related_field = True
        
        ret = self.env['sale.return'].search([])
        for rec in ret:
            if rec.company_id.id != user_company_id:
                rec.related_field = False
            else:
                rec.related_field = True
        
        quality_check = self.env['mrp.quality.check'].search([])
        for rec in quality_check:
            if (rec.company_id):
                if rec.company_id.id != user_company_id:
                    rec.related_field = False
                else:
                    rec.related_field = True
        
        for rec in self:
            rec.is_our_company = True

