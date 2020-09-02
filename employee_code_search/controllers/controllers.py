# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeCodeSearch(http.Controller):
#     @http.route('/employee_code_search/employee_code_search/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_code_search/employee_code_search/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_code_search.listing', {
#             'root': '/employee_code_search/employee_code_search',
#             'objects': http.request.env['employee_code_search.employee_code_search'].search([]),
#         })

#     @http.route('/employee_code_search/employee_code_search/objects/<model("employee_code_search.employee_code_search"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_code_search.object', {
#             'object': obj
#         })
