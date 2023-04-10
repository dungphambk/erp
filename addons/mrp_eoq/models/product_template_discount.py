from odoo import api, models, fields
from datetime import datetime, timedelta
from math import sqrt
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    price_1 = fields.Float(string='Price 1')
    minimum_amount_1 = fields.Float(string='Minimum Amount 1')
    total_cost_1 = fields.Float(string='Total Cost 1', compute='_compute_total_cost_1', store=True)
    optimal_amount_1 = fields.Float(string='Optimal Amount 1')

    price_2 = fields.Float(string='Price 2')
    minimum_amount_2 = fields.Float(string='Minimum Amount 2')
    total_cost_2 = fields.Float(string='Total Cost 2', compute='_compute_total_cost_2', store=True)
    optimal_amount_2 = fields.Float(string='Optimal Amount 2')

    price_3 = fields.Float(string='Price 3')
    minimum_amount_3 = fields.Float(string='Minimum Amount 3')
    total_cost_3 = fields.Float(string='Total Cost 3', compute='_compute_total_cost_3', store=True)
    optimal_amount_3 = fields.Float(string='Optimal Amount 3')

    lowest_cost = fields.Float(string="Lowest Cost")
    optimal_price = fields.Float(string='Optimal Price', compute='_compute_optimal_price', store=True)
    optimal_amount = fields.Float(string='Optimal Amount')

    @api.depends('price_1', 'minimum_amount_1', 'annual_demand', 'setup_cost', 'holding_cost')
    def _compute_total_cost_1(self):
        for product_template in self:
            if (product_template.holding_cost > 0):
                price = product_template.price_1
                minimum_amount = product_template.minimum_amount_1
                annual_demand = product_template.annual_demand
                setup_cost = product_template.setup_cost
                holding_cost = product_template.holding_cost

                optimal_quantity = sqrt((2 * annual_demand * setup_cost) / holding_cost)
                if (optimal_quantity < minimum_amount): optimal_quantity = minimum_amount

                if (optimal_quantity > 0):
                    setup_cost = annual_demand * setup_cost / optimal_quantity
                    holding_cost = optimal_quantity * holding_cost / 2
                    purchase_cost = price * annual_demand
                    product_template.total_cost_1 = setup_cost + holding_cost + purchase_cost
                    product_template.optimal_amount_1 = optimal_quantity

    @api.depends('price_2', 'minimum_amount_2', 'annual_demand', 'setup_cost', 'holding_cost')
    def _compute_total_cost_2(self):
        for product_template in self:
            if (product_template.holding_cost > 0):
                price = product_template.price_2
                minimum_amount = product_template.minimum_amount_2
                annual_demand = product_template.annual_demand
                setup_cost = product_template.setup_cost
                holding_cost = product_template.holding_cost
                
                optimal_quantity = sqrt((2 * annual_demand * setup_cost) / holding_cost)
                if (optimal_quantity < minimum_amount): optimal_quantity = minimum_amount

                if (optimal_quantity > 0):
                    setup_cost = annual_demand * setup_cost / optimal_quantity
                    holding_cost = optimal_quantity * holding_cost / 2
                    purchase_cost = price * annual_demand
                    product_template.total_cost_2 = setup_cost + holding_cost + purchase_cost
                    product_template.optimal_amount_2 = optimal_quantity

    @api.depends('price_3', 'minimum_amount_3', 'annual_demand', 'setup_cost', 'holding_cost')
    def _compute_total_cost_3(self):
        for product_template in self:
            if (product_template.holding_cost > 0):
                price = product_template.price_3
                minimum_amount = product_template.minimum_amount_3
                annual_demand = product_template.annual_demand
                setup_cost = product_template.setup_cost
                holding_cost = product_template.holding_cost
                
                optimal_quantity = sqrt((2 * annual_demand * setup_cost) / holding_cost)
                if (optimal_quantity < minimum_amount): optimal_quantity = minimum_amount

                if (optimal_quantity > 0):
                    setup_cost = annual_demand * setup_cost / optimal_quantity
                    holding_cost = optimal_quantity * holding_cost / 2
                    purchase_cost = price * annual_demand
                    product_template.total_cost_3 = setup_cost + holding_cost + purchase_cost
                    product_template.optimal_amount_3 = optimal_quantity
    
    @api.depends('total_cost_1', 'total_cost_2', 'total_cost_3')
    def _compute_optimal_price(self):
        for product_template in self:
            cost_1 = product_template.total_cost_1
            cost_2 = product_template.total_cost_2
            cost_3 = product_template.total_cost_3
            
            if (product_template.price_3 > 0):
                if (cost_1 < cost_2 and cost_1 < cost_3):
                    product_template.lowest_cost = cost_1
                    product_template.optimal_price = product_template.price_1
                    product_template.optimal_amount = product_template.optimal_amount_1
                elif (cost_2 < cost_1 and cost_2 < cost_3):
                    product_template.lowest_cost = cost_2
                    product_template.optimal_price = product_template.price_2
                    product_template.optimal_amount = product_template.optimal_amount_2
                else:
                    product_template.lowest_cost = cost_3
                    product_template.optimal_price = product_template.price_3
                    product_template.optimal_amount = product_template.optimal_amount_3
            else:
                if (cost_1 < cost_2):
                    product_template.lowest_cost = cost_1
                    product_template.optimal_price = product_template.price_1
                    product_template.optimal_amount = product_template.optimal_amount_1
                else:
                    product_template.lowest_cost = cost_2
                    product_template.optimal_price = product_template.price_2
                    product_template.optimal_amount = product_template.optimal_amount_2
    
    @api.constrains('price_1', 'price_2', 'price_3', 'minimum_amount_1', 'minimum_amount_2', 'minimum_amount_3')
    def _positive_field(self):
        for record in self:
            if record.price_1 < 0 or record.price_2 < 0 or record.price_3 < 0 or record.minimum_amount_1 < 0 or record.minimum_amount_2 < 0 or record.minimum_amount_3 < 0:
                raise UserError("Price and Amount must be positive")