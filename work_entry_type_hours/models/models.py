# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Hrwork_entry_type(models.Model):
    _inherit = 'hr.work.entry.type'

    date_start = fields.Datetime(string='From')
    date_stop = fields.Datetime(string='To')

class Hr_work_entry(models.Model):
    _inherit = 'hr.work.entry'

    @api.onchange('work_entry_type_id')
    def work_entry_time(self):
        for order in self:
            if order.work_entry_type_id:
                order.date_start = order.work_entry_type_id.date_start
                order.date_stop = order.work_entry_type_id.date_stop

