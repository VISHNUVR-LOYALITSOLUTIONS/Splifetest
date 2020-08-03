# -*- coding: utf-8 -*-
# from odoo import http


# class WorkEntryApprovalStage(http.Controller):
#     @http.route('/work_entry_approval_stage/work_entry_approval_stage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/work_entry_approval_stage/work_entry_approval_stage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('work_entry_approval_stage.listing', {
#             'root': '/work_entry_approval_stage/work_entry_approval_stage',
#             'objects': http.request.env['work_entry_approval_stage.work_entry_approval_stage'].search([]),
#         })

#     @http.route('/work_entry_approval_stage/work_entry_approval_stage/objects/<model("work_entry_approval_stage.work_entry_approval_stage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('work_entry_approval_stage.object', {
#             'object': obj
#         })
