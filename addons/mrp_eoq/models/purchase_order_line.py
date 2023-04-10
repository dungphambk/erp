from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def _compute_economic_order_quantity(self):
        for line in self:
            eoq = self.env['product.template'].search([
                ('id', '=', line.product_id.product_tmpl_id.id)
            ])
            line.optimal_amount = eoq.economic_order_quantity