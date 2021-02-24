# -*- coding: utf-8 -*-
from odoo import http

# class FiltroComercial(http.Controller):
#     @http.route('/filtro_comercial/filtro_comercial/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filtro_comercial/filtro_comercial/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('filtro_comercial.listing', {
#             'root': '/filtro_comercial/filtro_comercial',
#             'objects': http.request.env['filtro_comercial.filtro_comercial'].search([]),
#         })

#     @http.route('/filtro_comercial/filtro_comercial/objects/<model("filtro_comercial.filtro_comercial"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filtro_comercial.object', {
#             'object': obj
#         })