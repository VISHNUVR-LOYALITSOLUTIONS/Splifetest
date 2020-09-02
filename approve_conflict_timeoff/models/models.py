# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError

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
        if not self.time_off_type:
            raise ValidationError(_('For the approve time off please fill the Leave type.'))

        self.env['hr.leave.allocation'].create({
            'name': 'Compensatory Time Off',
            'employee_id': self.employee_id.id,
            'holiday_status_id': self.time_off_type.id,


            # 'duration_display':self.duration,



            # 'number_of_hours_display': self.duration,
            # # 'allocation_type': 'accrual',
            # 'number_of_days': 1,
            # 'number_per_interval': 1,
            # 'interval_number': 1,
            # 'unit_per_interval': 'days',
            # 'interval_unit': 'weeks',
            # 'date_from': self.date_start,
            # 'date_to': self.date_stop,
            # 'request_date_from': datetime.strptime(str(self.date_start), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d'),
            # 'request_date_to': datetime.strptime(str(self.date_stop), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d'),
            # 'number_of_days': self.duration,
        })

        # so = self.env['hr.leave'].create(so_order)
        return res



