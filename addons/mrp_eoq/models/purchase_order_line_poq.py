from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    production_order_quantity = fields.Float(string='Production Order Quantity', compute='_compute_production_order_quantity', store=False)

    def _compute_production_order_quantity(self):
        for line in self:
            template = self.env['product.template'].search([
                ('id', '=', line.product_id.product_tmpl_id.id)
            ])
            line.production_order_quantity = template.production_order_quantity