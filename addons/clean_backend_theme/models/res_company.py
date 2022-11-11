import base64
from odoo import api, fields, models, tools
from ..hooks import replace_menu_icon


class Company(models.Model):
    _inherit = "res.company"

    sidebar_logo = fields.Binary("Sidebar Logo")
    sidebar_logo_web = fields.Binary(compute='_compute_sidebar_logo_web', store=True, attachment=False)

    @api.depends('sidebar_logo')
    def _compute_sidebar_logo_web(self):
        for company in self:
            img = company.sidebar_logo
            company.sidebar_logo_web = img and base64.b64encode(tools.image_process(base64.b64decode(img), size=(180, 0)))

    def refresh_menu_icon(self):
        self.ensure_one()
        replace_menu_icon(self.env['ir.ui.menu'].search([('parent_id', '=', False)]))
        return True
