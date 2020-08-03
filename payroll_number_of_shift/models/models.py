# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Hrpayroll(models.Model):
    _inherit = 'hr.payslip.worked_days'

    no_of_shift = fields.Float("No.of Shift",compute='no_of_shift_count')

    @api.depends('work_entry_type_id','work_entry_type_id.no_of_hours','number_of_days', 'number_of_hours')
    @api.onchange('work_entry_type_id', 'number_of_days', 'number_of_hours')
    def no_of_shift_count(self):
        for i in self:
            if i.number_of_hours:
                i.no_of_shift = (i.number_of_hours/i.work_entry_type_id.no_of_hours) if i.work_entry_type_id.no_of_hours!=0 else 0.0
            else:
                i.no_of_shift=0.0



class Hrwork_entry_type(models.Model):
    _inherit = 'hr.work.entry.type'

    no_of_hours = fields.Float("Hours")

