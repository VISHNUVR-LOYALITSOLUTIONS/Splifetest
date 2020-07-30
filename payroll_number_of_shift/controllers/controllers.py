# -*- coding: utf-8 -*-
# from odoo import http


# class PayrollNumberOfShift(http.Controller):
#     @http.route('/payroll_number_of_shift/payroll_number_of_shift/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payroll_number_of_shift/payroll_number_of_shift/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('payroll_number_of_shift.listing', {
#             'root': '/payroll_number_of_shift/payroll_number_of_shift',
#             'objects': http.request.env['payroll_number_of_shift.payroll_number_of_shift'].search([]),
#         })

#     @http.route('/payroll_number_of_shift/payroll_number_of_shift/objects/<model("payroll_number_of_shift.payroll_number_of_shift"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payroll_number_of_shift.object', {
#             'object': obj
#         })
