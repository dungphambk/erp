# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _
from odoo.exceptions import UserError

class MrpProductionLine(models.Model):
    _name = "mrp.production.line"
    _description = "Production Line"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    order_id = fields.Many2one('mrp.production', string="Manufacturing Order", domain="[('state','in', ('confirmed', 'progress', 'to_close'))]")
    manager_id = fields.Many2one('res.users', string="Manager", default=lambda self: self.env.user)
    start_date = fields.Datetime(string="Start Date Of Current Task")
    state = fields.Selection([
        ("available", "Available"),
        ("inprogress", "In Progress"),
        ("closed", "Closed"),
    ], string="State", default="available")
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True,
        default=lambda self: self.env.company)
    is_our_company = fields.Boolean(string='Is Our Company', compute='_compute_is_our_company', store=False)
    related_field = fields.Boolean(string='Related Field', related='is_our_company', store=True)
    
    def _compute_is_our_company(self):
        user_company_id = self.env.user.company_id.id
        quality_check = self.env['mrp.production.line'].search([])
        for rec in quality_check:
            if rec.company_id.id != user_company_id:
                rec.is_our_company = False
                rec.related_field = False
            else:
                rec.is_our_company = True
                rec.related_field = True

    def action_done(self):
        log = self.env['mrp.production.log'].search([
            ('order_id', '=', self.order_id.id),
            ('state','=','inprogress'),
        ])
        log.write({'finish_date': fields.Datetime.now(), 'state': 'done'})
        return self.write({'state': 'available', 'order_id': None, 'start_date': None})

    def action_assign_task(self):
        log_done = self.env['mrp.production.log'].search([
            ('order_id', '=', self.order_id.id),
            ('state', '=', 'done'),
        ])
        if log_done:
            raise UserError('This order has already been produced')
        log_inprogress = self.env['mrp.production.log'].search([
            ('order_id', '=', self.order_id.id),
            ('state', '=', 'inprogress'),
        ])
        if log_inprogress:
            raise UserError('This order has already been working on at another line')
        self.env['mrp.production.log'].create({
            'order_id': self.order_id.id,
            'start_date': fields.Datetime.now(),
        })
        return self.write({'state': 'inprogress', 'start_date': fields.Datetime.now()})

    def action_cancel_task(self):
        if self.order_id == None:
            raise UserError('There is no task assigned to this line')
        log = self.env['mrp.production.log'].search([
            ('order_id', '=', self.order_id.id),
            ('state','=','inprogress'),
        ])
        log.write({'finish_date': fields.Datetime.now(), 'state': 'cancel'})
        return self.write({'state': 'available', 'order_id': None, 'start_date': None})
    
    def action_close_line(self):
        log = self.env['mrp.production.log'].search([
            ('order_id', '=', self.order_id.id),
            ('state','=','inprogress'),
        ])
        log.write({'state': 'cancel'})
        return self.write({'state': 'closed', 'order_id': None, 'start_date': None})

    def action_reopen_line(self):
        return self.write({'state': 'available', 'order_id': None, 'start_date': None})
