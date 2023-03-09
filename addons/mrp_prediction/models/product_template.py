from odoo import models, fields, api
from datetime import datetime, timedelta

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    next_month_requirement = fields.Float(
        string='Next Month Requirement',
        compute='_compute_next_month_requirement',
        store=False,
        help='The predicted requirement for the next month based on the last 3 months\' sales order.'
    )

    qty_available = fields.Float(string='On-hand Quantity', compute='_compute_qty_available', store=False)

    shortage_surplus = fields.Float(string='Shortage / Surplus', compute='_compute_shortage_surplus', store=False)

    product_profit = fields.Float(string='Product Profit', compute='_compute_product_profit', store=False)

    def _compute_next_month_requirement(self):
        for product_template in self:
            last_3_months = datetime.now() - timedelta(days=90)
            sale_lines = self.env['sale.order.line'].search([
                ('order_id.date_order', '>=', last_3_months),
                ('product_id.product_tmpl_id', '=', product_template.id)
            ])
            total_qty = sum(sale_lines.mapped('product_uom_qty'))
            avg_qty_per_month = total_qty / 3 if total_qty > 0 else 0
            product_template.next_month_requirement = avg_qty_per_month
    
    @api.depends('product_variant_ids', 'product_variant_ids.qty_available')
    def _compute_qty_available(self):
        for product_template in self:
            qty_available = sum(product_template.product_variant_ids.mapped('qty_available'))
            product_template.qty_available = qty_available
    
    def _compute_shortage_surplus(self):
        for product_template in self:
            product_template.shortage_surplus = product_template.qty_available - product_template.next_month_requirement
    
    def _compute_product_profit(self):
        for product_template in self:
            product_template.product_profit = product_template.list_price - product_template.standard_price