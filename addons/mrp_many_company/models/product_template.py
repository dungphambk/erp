from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True,
        default=lambda self: self.env.company)
