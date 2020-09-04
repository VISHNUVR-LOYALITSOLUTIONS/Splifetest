# -*- coding: utf-8 -*-
# from odoo import http


# class SelectiveWorkentryTimesheet(http.Controller):
#     @http.route('/selective_workentry_timesheet/selective_workentry_timesheet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/selective_workentry_timesheet/selective_workentry_timesheet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('selective_workentry_timesheet.listing', {
#             'root': '/selective_workentry_timesheet/selective_workentry_timesheet',
#             'objects': http.request.env['selective_workentry_timesheet.selective_workentry_timesheet'].search([]),
#         })

#     @http.route('/selective_workentry_timesheet/selective_workentry_timesheet/objects/<model("selective_workentry_timesheet.selective_workentry_timesheet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('selective_workentry_timesheet.object', {
#             'object': obj
#         })
