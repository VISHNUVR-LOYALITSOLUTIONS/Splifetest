# -*- coding: utf-8 -*-
# from odoo import http


# class ApproveConflictTimeoff(http.Controller):
#     @http.route('/approve_conflict_timeoff/approve_conflict_timeoff/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/approve_conflict_timeoff/approve_conflict_timeoff/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('approve_conflict_timeoff.listing', {
#             'root': '/approve_conflict_timeoff/approve_conflict_timeoff',
#             'objects': http.request.env['approve_conflict_timeoff.approve_conflict_timeoff'].search([]),
#         })

#     @http.route('/approve_conflict_timeoff/approve_conflict_timeoff/objects/<model("approve_conflict_timeoff.approve_conflict_timeoff"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('approve_conflict_timeoff.object', {
#             'object': obj
#         })
