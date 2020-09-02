# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectSearch(http.Controller):
#     @http.route('/project_search/project_search/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_search/project_search/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_search.listing', {
#             'root': '/project_search/project_search',
#             'objects': http.request.env['project_search.project_search'].search([]),
#         })

#     @http.route('/project_search/project_search/objects/<model("project_search.project_search"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_search.object', {
#             'object': obj
#         })
