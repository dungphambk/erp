# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _

class MrpQualityCheck(models.Model):
    _name = "mrp.quality.check"
    _description = "Quality Check"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Reference", default=lambda self: _('New'))
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
    warning = fields.Char(string = "Please check the Quality Control first")

    def action_confirm(self):
        return self.write({'state': 'inprogress'})

    def action_pass(self):
        return self.write({'state': 'pass'})
    
    def action_fail(self):
        return self.write({'state': 'fail'})

