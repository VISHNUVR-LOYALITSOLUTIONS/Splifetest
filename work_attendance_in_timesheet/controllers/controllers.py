# -*- coding: utf-8 -*-
# from odoo import http


# class WorkAttendanceInTimesheet(http.Controller):
#     @http.route('/work_attendance_in_timesheet/work_attendance_in_timesheet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/work_attendance_in_timesheet/work_attendance_in_timesheet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('work_attendance_in_timesheet.listing', {
#             'root': '/work_attendance_in_timesheet/work_attendance_in_timesheet',
#             'objects': http.request.env['work_attendance_in_timesheet.work_attendance_in_timesheet'].search([]),
#         })

#     @http.route('/work_attendance_in_timesheet/work_attendance_in_timesheet/objects/<model("work_attendance_in_timesheet.work_attendance_in_timesheet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('work_attendance_in_timesheet.object', {
#             'object': obj
#         })
