# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
class ChangeupdateState(models.TransientModel):
    _name = 'update.state.val'
    _description = 'Change the state of sale order'


    state = fields.Selection([
        ('draft', 'Draft'),
        ('validated', 'Validated'),
        ('conflict', 'Conflict'),
        ('cancelled', 'Cancelled'),
        ('button_validate_approval', 'Validate Approval'),
    ], string = 'Status')
    def update_state(self):
        active_ids = self._context.get('active_ids', []) or []
        work = self.env['hr.work.entry'].browse(active_ids)
        # work = self.env['hr.work.entry'].search([('state', '!=', 'validated')])
        for record in work.search([('state', '!=', 'validated')]).browse(active_ids):
            record.state = self.state
