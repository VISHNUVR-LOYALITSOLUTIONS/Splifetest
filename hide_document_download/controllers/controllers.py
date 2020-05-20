# -*- coding: utf-8 -*-
# from odoo import http


# class HideDocumentDownload(http.Controller):
#     @http.route('/hide_document_download/hide_document_download/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hide_document_download/hide_document_download/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hide_document_download.listing', {
#             'root': '/hide_document_download/hide_document_download',
#             'objects': http.request.env['hide_document_download.hide_document_download'].search([]),
#         })

#     @http.route('/hide_document_download/hide_document_download/objects/<model("hide_document_download.hide_document_download"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hide_document_download.object', {
#             'object': obj
#         })
