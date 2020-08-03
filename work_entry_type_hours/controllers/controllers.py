# -*- coding: utf-8 -*-
# from odoo import http


# class WorkEntryTypeHours(http.Controller):
#     @http.route('/work_entry_type_hours/work_entry_type_hours/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/work_entry_type_hours/work_entry_type_hours/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('work_entry_type_hours.listing', {
#             'root': '/work_entry_type_hours/work_entry_type_hours',
#             'objects': http.request.env['work_entry_type_hours.work_entry_type_hours'].search([]),
#         })

#     @http.route('/work_entry_type_hours/work_entry_type_hours/objects/<model("work_entry_type_hours.work_entry_type_hours"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('work_entry_type_hours.object', {
#             'object': obj
#         })
