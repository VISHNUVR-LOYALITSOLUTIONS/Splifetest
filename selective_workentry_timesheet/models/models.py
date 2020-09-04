# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
class Selective_work_entry(models.TransientModel):
    _name = 'select.workentry.timesheet'
    _description = 'Timesheet for Work entry'

    def update_timesheet(self):
        active_ids = self._context.get('active_ids', []) or []
        work = self.env['hr.work.entry'].browse(active_ids)
        # work = self.env['hr.work.entry'].search([('state', '!=', 'validated')])
        for record in work.search([('total_work_attendance','=',0.0)]).browse(active_ids):
            record.action_view_work()
            # return record
