# -*- coding: utf-8 -*-
# from odoo import http


# class SplifeInvoicePrint(http.Controller):
#     @http.route('/splife_invoice_print/splife_invoice_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/splife_invoice_print/splife_invoice_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('splife_invoice_print.listing', {
#             'root': '/splife_invoice_print/splife_invoice_print',
#             'objects': http.request.env['splife_invoice_print.splife_invoice_print'].search([]),
#         })

#     @http.route('/splife_invoice_print/splife_invoice_print/objects/<model("splife_invoice_print.splife_invoice_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('splife_invoice_print.object', {
#             'object': obj
#         })
