# -*- coding: utf-8 -*-
# from odoo import http


# class SaleCustomisation(http.Controller):
#     @http.route('/sale_customisation/sale_customisation', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_customisation/sale_customisation/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_customisation.listing', {
#             'root': '/sale_customisation/sale_customisation',
#             'objects': http.request.env['sale_customisation.sale_customisation'].search([]),
#         })

#     @http.route('/sale_customisation/sale_customisation/objects/<model("sale_customisation.sale_customisation"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_customisation.object', {
#             'object': obj
#         })

