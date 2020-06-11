# -*- coding: utf-8 -*-
# from odoo import http


# class RoomChartManagement(http.Controller):
#     @http.route('/room_chart_management/room_chart_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/room_chart_management/room_chart_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('room_chart_management.listing', {
#             'root': '/room_chart_management/room_chart_management',
#             'objects': http.request.env['room_chart_management.room_chart_management'].search([]),
#         })

#     @http.route('/room_chart_management/room_chart_management/objects/<model("room_chart_management.room_chart_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('room_chart_management.object', {
#             'object': obj
#         })
