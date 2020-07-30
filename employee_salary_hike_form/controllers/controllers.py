# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeSalaryHikeForm(http.Controller):
#     @http.route('/employee_salary_hike_form/employee_salary_hike_form/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_salary_hike_form/employee_salary_hike_form/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_salary_hike_form.listing', {
#             'root': '/employee_salary_hike_form/employee_salary_hike_form',
#             'objects': http.request.env['employee_salary_hike_form.employee_salary_hike_form'].search([]),
#         })

#     @http.route('/employee_salary_hike_form/employee_salary_hike_form/objects/<model("employee_salary_hike_form.employee_salary_hike_form"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_salary_hike_form.object', {
#             'object': obj
#         })
