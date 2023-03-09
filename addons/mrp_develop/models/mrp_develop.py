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