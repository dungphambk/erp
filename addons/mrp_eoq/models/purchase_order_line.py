from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    economic_order_quantity = fields.Float(string='Economic Order Quantity', compute='_compute_economic_order_quantity', store=False)

    def _compute_economic_order_quantity(self):
        for line in self:
            eoq = self.env['product.template'].search([
                ('id', '=', line.product_id.product_tmpl_id.id)
            ])
            line.economic_order_quantity = eoq.economic_order_quantity