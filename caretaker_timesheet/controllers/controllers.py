# -*- coding: utf-8 -*-
# from odoo import http


# class CaretakerTimesheet(http.Controller):
#     @http.route('/caretaker_timesheet/caretaker_timesheet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/caretaker_timesheet/caretaker_timesheet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('caretaker_timesheet.listing', {
#             'root': '/caretaker_timesheet/caretaker_timesheet',
#             'objects': http.request.env['caretaker_timesheet.caretaker_timesheet'].search([]),
#         })

#     @http.route('/caretaker_timesheet/caretaker_timesheet/objects/<model("caretaker_timesheet.caretaker_timesheet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('caretaker_timesheet.object', {
#             'object': obj
#         })
