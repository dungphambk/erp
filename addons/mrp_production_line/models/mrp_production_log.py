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

