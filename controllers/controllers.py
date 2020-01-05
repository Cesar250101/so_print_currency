# -*- coding: utf-8 -*-
from odoo import http

# class PoPrintCurrency(http.Controller):
#     @http.route('/po_print_currency/po_print_currency/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/po_print_currency/po_print_currency/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('po_print_currency.listing', {
#             'root': '/po_print_currency/po_print_currency',
#             'objects': http.request.env['po_print_currency.po_print_currency'].search([]),
#         })

#     @http.route('/po_print_currency/po_print_currency/objects/<model("po_print_currency.po_print_currency"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('po_print_currency.object', {
#             'object': obj
#         })