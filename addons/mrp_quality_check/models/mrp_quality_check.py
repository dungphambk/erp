# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _

class MrpQualityCheck(models.Model):
    _name = "mrp.quality.check"
    _description = "Quality Check"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Reference")
    description = fields.Text(string="Description")
    order_id = fields.Many2one('mrp.production', string="Manufacturing Order", domain="[('state','in', ('confirmed', 'progress', 'to_close'))]")
    user_id = fields.Many2one('res.users', string="Responsible", default=lambda self: self.env.user)
    create_date = fields.Datetime(string="Create Date")
    image = fields.Binary(string = "Image")
    state = fields.Selection([
        ("draft", "Draft"),
        ("inprogress", "In Progress"),
        ("pass", "Pass"),
        ("fail", "Fail"),
    ], string="State", default="draft")
    warning = fields.Char(string = "warning")
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True,
        default=lambda self: self.env.company)
    is_our_company = fields.Boolean(string='Is Our Company', compute='_compute_is_our_company', store=False)
    related_field = fields.Boolean(string='Related Field', related='is_our_company', store=True)
    
    def _compute_is_our_company(self):
        user_company_id = self.env.user.company_id.id
        print("1")
        quality_check = self.env['mrp.quality.check'].search([])
        for rec in quality_check:
            if (rec.company_id):
                if rec.company_id.id != user_company_id:
                    rec.is_our_company = False
                    rec.related_field = False
                else:
                    rec.is_our_company = True
                    rec.related_field = True

    def action_confirm(self):
        return self.write({'state': 'inprogress'})

    def action_pass(self):
        return self.write({'state': 'pass'})
    
    def action_fail(self):
        return self.write({'state': 'fail'})

