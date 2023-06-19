from odoo import models, fields
from datetime import datetime, timedelta
import math
import random

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    annual_demand = fields.Float(string='Annual Demand', compute='_compute_annual_demand', store=False)

    setup_cost = fields.Float(string='Setup Cost', default = random.randint(50,300))

    holding_cost = fields.Float(string='Holding Cost', default = random.randint(1,15))

    economic_order_quantity = fields.Float(string='Economic Order Quantity', compute='_compute_economic_order_quantity', store=False)

    setup = fields.Float(string = "Total Setup Cost")

    holding = fields.Float(string = "Total Holding Cost")

    purchase = fields.Float(string = "Total Purchase Cost")

    total = fields.Float(string = "Total Cost")

    def _compute_annual_demand(self):
        for product_template in self:
            last_year = datetime.now() - timedelta(days=365)
            sale_lines = self.env['sale.order.line'].search([
                ('order_id.date_order', '>=', last_year),
                ('product_id.product_tmpl_id', '=', product_template.id)
            ])
            total_qty = sum(sale_lines.mapped('product_uom_qty'))
            product_template.annual_demand = total_qty
    
    def _compute_economic_order_quantity(self):
        for product_template in self:
            product_template.setup = 0
            product_template.holding = 0
            product_template.purchase = 0
            product_template.total = 0
            if (product_template.holding_cost >0 and product_template.daily_production_rate == 0):
                annual_demand = product_template.annual_demand
                setup_cost = product_template.setup_cost
                holding_cost = product_template.holding_cost
                product_template.economic_order_quantity = math.ceil(math.sqrt((2 * product_template.annual_demand * product_template.setup_cost) / product_template.holding_cost))
                if product_template.economic_order_quantity > 0: product_template.setup = annual_demand * setup_cost / product_template.economic_order_quantity
                product_template.holding = product_template.economic_order_quantity * holding_cost / 2
                product_template.purchase = product_template.list_price * annual_demand
                product_template.total = product_template.setup + product_template.holding + product_template.purchase
            else: 
                product_template.economic_order_quantity = 0
                