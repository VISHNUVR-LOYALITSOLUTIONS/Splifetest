# -*- coding: utf-8 -*-
# from odoo import http


# class CompanyWiseFieldSecurity(http.Controller):
#     @http.route('/company_wise_field_security/company_wise_field_security/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/company_wise_field_security/company_wise_field_security/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('company_wise_field_security.listing', {
#             'root': '/company_wise_field_security/company_wise_field_security',
#             'objects': http.request.env['company_wise_field_security.company_wise_field_security'].search([]),
#         })

#     @http.route('/company_wise_field_security/company_wise_field_security/objects/<model("company_wise_field_security.company_wise_field_security"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('company_wise_field_security.object', {
#             'object': obj
#         })
