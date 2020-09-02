# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Hr_work_entry(models.Model):
    _inherit = 'hr.work.entry'

    state = fields.Selection(selection_add=[('button_validate_approval', 'Validate Approval')])

    def button_validate_approval(self):
        for order in self:
            order.write({'state': 'button_validate_approval'})


