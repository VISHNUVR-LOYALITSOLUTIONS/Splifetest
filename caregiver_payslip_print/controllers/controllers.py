# -*- coding: utf-8 -*-
# from odoo import http


# class CaregiverPayslipPrint(http.Controller):
#     @http.route('/caregiver_payslip_print/caregiver_payslip_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/caregiver_payslip_print/caregiver_payslip_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('caregiver_payslip_print.listing', {
#             'root': '/caregiver_payslip_print/caregiver_payslip_print',
#             'objects': http.request.env['caregiver_payslip_print.caregiver_payslip_print'].search([]),
#         })

#     @http.route('/caregiver_payslip_print/caregiver_payslip_print/objects/<model("caregiver_payslip_print.caregiver_payslip_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('caregiver_payslip_print.object', {
#             'object': obj
#         })
