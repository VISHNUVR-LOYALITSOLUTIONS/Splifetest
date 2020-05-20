# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    document_hide = fields.Boolean('Allow Document Download', default=True)

    def user_access(self):
        users = self.env.uid
        flag=False
        user_document = self.env['res.users'].browse(users).document_hide

        if users:


            if user_document == True:
                flag = True
            else:
                flag = False
        return flag

class Documents(models.Model):
    _inherit = 'documents.document'


    def user_access(self):
        users = self.env.uid
        flag=False
        user_document = self.env['res.users'].browse(users).document_hide

        if users:


            if user_document == True:
                flag = True
            else:
                flag = False
        return flag
