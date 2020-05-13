# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from datetime import date, timedelta


class Approve_Conflict(models.Model):
    _inherit = 'hr.work.entry'

    time_off_type = fields.Many2one('hr.leave.type','Leave Type')



    def action_approve_leave(self):
        res = super(Approve_Conflict, self).action_approve_leave()

        hr_leaves = self.env['hr.leave'].search([('employee_id','=',self.employee_id.id),
         ('request_date_from','=',datetime.strptime(str(self.date_start), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')),
         ('request_date_to','=',datetime.strptime(str(self.date_stop), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d'))])
        for i in hr_leaves:
            i.state = 'draft'
        hr_leaves.unlink()
        self.env['hr.leave'].create({
            'name': 'Compensatory Time Off',
            'employee_id': self.employee_id.id,
            'holiday_status_id': self.time_off_type.id,
            'date_from': self.date_start,
            'date_to': self.date_stop,
            'request_date_from': datetime.strptime(str(self.date_start), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d'),
            'request_date_to': datetime.strptime(str(self.date_stop), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d'),
            # 'number_of_days': self.duration,
        })

        # so = self.env['hr.leave'].create(so_order)
        return res



