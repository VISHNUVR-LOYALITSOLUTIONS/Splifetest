# -*- coding: utf-8 -*-
# from odoo import http


# class DepartmentWiseRestriction(http.Controller):
#     @http.route('/department_wise_restriction/department_wise_restriction/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/department_wise_restriction/department_wise_restriction/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('department_wise_restriction.listing', {
#             'root': '/department_wise_restriction/department_wise_restriction',
#             'objects': http.request.env['department_wise_restriction.department_wise_restriction'].search([]),
#         })

#     @http.route('/department_wise_restriction/department_wise_restriction/objects/<model("department_wise_restriction.department_wise_restriction"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('department_wise_restriction.object', {
#             'object': obj
#         })
