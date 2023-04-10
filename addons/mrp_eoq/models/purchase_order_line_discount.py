from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    optimal_price = fields.Float(string='Optimal Price', compute='_compute_optimal_price', store=False)
    optimal_amount = fields.Float(string='Optimal Price', compute='_compute_optimal_amount', store=False)

    def _compute_optimal_price(self):
        for line in self:
            template = self.env['product.template'].search([
                ('id', '=', line.product_id.product_tmpl_id.id)
            ])
            line.optimal_price = template.optimal_price
    
    def _compute_optimal_amount(self):
        for line in self:
            template = self.env['product.template'].search([
                ('id', '=', line.product_id.product_tmpl_id.id)
            ])
            line.optimal_amount = template.optimal_amount
    
    
