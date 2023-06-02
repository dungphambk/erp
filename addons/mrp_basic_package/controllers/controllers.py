# -*- coding: utf-8 -*-
# from odoo import http


# class MrpEoqPoq(http.Controller):
#     @http.route('/mrp_eoq_poq/mrp_eoq_poq', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mrp_eoq_poq/mrp_eoq_poq/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mrp_eoq_poq.listing', {
#             'root': '/mrp_eoq_poq/mrp_eoq_poq',
#             'objects': http.request.env['mrp_eoq_poq.mrp_eoq_poq'].search([]),
#         })

#     @http.route('/mrp_eoq_poq/mrp_eoq_poq/objects/<model("mrp_eoq_poq.mrp_eoq_poq"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mrp_eoq_poq.object', {
#             'object': obj
#         })
