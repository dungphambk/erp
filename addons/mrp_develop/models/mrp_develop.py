# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError
from odoo.tools import float_compare, float_round
from odoo.osv import expression

from collections import defaultdict


class MrpDevelop(models.Model):
    _name = "mrp.develop"
    _description = "Develop"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    category = fields.Text(string="Category")
    created_by = fields.Many2one("res.users", string="Created By")
    status = fields.Selection([
        ("idea", "Idea"),
        ("inprogress", "In Progress"),
        ("done", "Done")
    ], string="Status", default="idea")
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True,
        default=lambda self: self.env.company)
    is_our_company = fields.Boolean(string='Is Our Company', compute='_compute_is_our_company', store=False)
    related_field = fields.Boolean(string='Related Field', related='is_our_company', store=True)
    
    def _compute_is_our_company(self):
        user_company_id = self.env.user.company_id.id
        quality_check = self.env['mrp.develop'].search([])
        for rec in quality_check:
            if (rec.company_id):
                if rec.company_id.id != user_company_id:
                    rec.is_our_company = False
                    rec.related_field = False
                else:
                    rec.is_our_company = True
                    rec.related_field = True