# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _

class MrpProductionLog(models.Model):
    _name = "mrp.production.log"
    _description = "Production Log"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    order_id = fields.Many2one('mrp.production', string="Manufacturing Order", required= True, domain="[('state','in', ('confirmed', 'progress', 'to_close'))]")
    start_date = fields.Datetime(string="Start Date")
    finish_date = fields.Datetime(string="Finish Date")
    state = fields.Selection([
        ("inprogress", "In Progress"),
        ("done", "Done"),
        ("cancel", "Cancel")
    ], string="State", default="inprogress")
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True,
        default=lambda self: self.env.company)
    is_our_company = fields.Boolean(string='Is Our Company', compute='_compute_is_our_company', store=False)
    related_field = fields.Boolean(string='Related Field', related='is_our_company', store=True)
    
    def _compute_is_our_company(self):
        user_company_id = self.env.user.company_id.id
        quality_check = self.env['mrp.production.log'].search([])
        for rec in quality_check:
            if rec.company_id.id != user_company_id:
                rec.is_our_company = False
                rec.related_field = False
            else:
                rec.is_our_company = True
                rec.related_field = True

