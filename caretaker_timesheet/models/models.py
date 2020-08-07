# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'


    search_id = fields.Char(string="Code No.",related='project_id.project_code')
    rate_per_shift = fields.Float(string="Rate Per Shift", related='project_id.rate_per_shift')
    no_of_shift = fields.Float(string="No of Shifts Per day requested")
    payment_amount = fields.Float(string="Payment",compute='payment_amount_calc',store=True)

    total_no_of_shift = fields.Float(string="Total No of Shift")

    @api.onchange('work_entry_type')
    def onchange_amount_calc(self):
        for i in self:
            if i.work_entry_type:
                i.no_of_shift = i.work_entry_type.no_of_shift
                i.total_no_of_shift = i.work_entry_type.no_of_shift

    @api.depends('rate_per_shift','no_of_shift')
    def payment_amount_calc(self):
        for i in self:
            if i.no_of_shift or i.rate_per_shift:
                i.payment_amount = i.no_of_shift * i.rate_per_shift


class Hrprojects(models.Model):
    _inherit = 'hr.work.entry'



    def action_view_work(self):

        res = super(Hrprojects, self).action_view_work()

        res.write({
            'search_id': self.project_id.project_code,
            'rate_per_shift': self.project_id.rate_per_shift,
            'no_of_shift': self.work_entry_type_id.no_of_shift,
            'payment_amount': self.work_entry_type_id.no_of_shift*self.project_id.rate_per_shift,
            'total_no_of_shift':self.work_entry_type_id.no_of_shift
        })
        return res

