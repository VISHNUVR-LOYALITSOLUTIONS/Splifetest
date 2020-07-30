# -*- coding: utf-8 -*-
# from odoo import http


# class ConflictHolidayWorkentry(http.Controller):
#     @http.route('/conflict_holiday_workentry/conflict_holiday_workentry/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/conflict_holiday_workentry/conflict_holiday_workentry/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('conflict_holiday_workentry.listing', {
#             'root': '/conflict_holiday_workentry/conflict_holiday_workentry',
#             'objects': http.request.env['conflict_holiday_workentry.conflict_holiday_workentry'].search([]),
#         })

#     @http.route('/conflict_holiday_workentry/conflict_holiday_workentry/objects/<model("conflict_holiday_workentry.conflict_holiday_workentry"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('conflict_holiday_workentry.object', {
#             'object': obj
#         })
