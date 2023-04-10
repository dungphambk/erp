from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def _compute_production_order_quantity(self):
        for line in self:
            template = self.env['product.template'].search([
                ('id', '=', line.product_id.product_tmpl_id.id)
            ])
            line.optimal_amount = template.production_order_quantity