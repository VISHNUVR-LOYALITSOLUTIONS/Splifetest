# -*- coding: utf-8 -*-
# from odoo import http


# class RecruitmentQuestionsForm(http.Controller):
#     @http.route('/recruitment_questions_form/recruitment_questions_form/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/recruitment_questions_form/recruitment_questions_form/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('recruitment_questions_form.listing', {
#             'root': '/recruitment_questions_form/recruitment_questions_form',
#             'objects': http.request.env['recruitment_questions_form.recruitment_questions_form'].search([]),
#         })

#     @http.route('/recruitment_questions_form/recruitment_questions_form/objects/<model("recruitment_questions_form.recruitment_questions_form"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('recruitment_questions_form.object', {
#             'object': obj
#         })
