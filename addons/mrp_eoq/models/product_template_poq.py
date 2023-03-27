from odoo import api, models, fields
from datetime import datetime, timedelta
from math import sqrt
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    daily_production_rate = fields.Float(string='Daily Production Rate', compute='_compute_daily_production', store=False)

    daily_demand_rate = fields.Float(string='Daily Demand Rate', compute='_compute_daily_demand', store=False)

    production_order_quantity = fields.Float(string='Production Order Quantity', compute='_compute_production_order_quantity', store=False)

    def _compute_daily_production(self):
        today = fields.Date.today()
        last_year = today - timedelta(days=365)
        for product_template in self:
            production_qty = 0.0
            for product_variant in product_template.product_variant_ids:
                production_moves = self.env['stock.move'].search([
                    ('product_id', '=', product_variant.id),
                    ('state', '=', 'done'),
                    ('production_id', '!=', False),
                    ('date', '>=', last_year),
                    ('date', '<=', today),
                ])
                production_qty += sum(production_moves.mapped('production_id.qty_produced'))
            product_template.daily_production_rate = production_qty / 365

    def _compute_daily_demand(self):
        for product_template in self:
            daily_demand = product_template.annual_demand / 365
            product_template.daily_demand_rate = daily_demand

    def _compute_production_order_quantity(self):
        for product_template in self:
            if (product_template.holding_cost >0 and product_template.daily_production_rate > product_template.daily_demand_rate):
                product_template.production_order_quantity = sqrt((2 * product_template.annual_demand * product_template.setup_cost) / product_template.holding_cost * (product_template.daily_production_rate / (product_template.daily_production_rate - product_template.daily_demand_rate)))
            else: product_template.production_order_quantity = 0
    
    @api.constrains('setup_cost', 'holding_cost', 'daily_production_rate', 'daily_demand_rate')
    def _positive_field(self):
        for record in self:
            if record.setup_cost < 0 or record.holding_cost < 0 or record.daily_production_rate < 0 or record.daily_demand_rate < 0:
                raise UserError("Fields must be positive")