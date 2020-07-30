# -*- coding: utf-8 -*-
# from odoo import http


# class HrDashboard(http.Controller):
#     @http.route('/hr_dashboard/hr_dashboard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_dashboard/hr_dashboard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_dashboard.listing', {
#             'root': '/hr_dashboard/hr_dashboard',
#             'objects': http.request.env['hr_dashboard.hr_dashboard'].search([]),
#         })

#     @http.route('/hr_dashboard/hr_dashboard/objects/<model("hr_dashboard.hr_dashboard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_dashboard.object', {
#             'object': obj
#         })
