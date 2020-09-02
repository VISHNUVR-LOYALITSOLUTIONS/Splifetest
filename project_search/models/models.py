# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Project(models.Model):
    _inherit = 'project.project'

    project_code = fields.Char("Search ID")

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if name:
            # Be sure name_search is symetric to name_get
            name = name.split(' / ')[-1]
            args = ['|', '|', ('project_code', operator, name), ('name', operator, name), ('id', operator, name)] + args
        partner_category_ids = self._search(args, limit=limit, access_rights_uid=name_get_uid)
        return models.lazy_name_get(self.browse(partner_category_ids).with_user(name_get_uid))

