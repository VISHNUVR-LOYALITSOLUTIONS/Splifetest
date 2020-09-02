# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResUsers(models.Model):

    _inherit = "res.users"

    department_ids = fields.Many2many(comodel_name="hr.department",string="Departments")

class Hrwork_entry_type(models.Model):
    _inherit = 'hr.work.entry.type'

    department_id = fields.Many2many(comodel_name="hr.department",string="Department")

class Hr_work_entry(models.Model):
    _inherit = 'hr.work.entry'

    department_id = fields.Many2one(comodel_name="hr.department",string="Department",related='employee_id.department_id')

class HrPayslip(models.Model):
    _inherit  = 'hr.payslip'

    department_id = fields.Many2one(comodel_name="hr.department",string="Department",related='employee_id.department_id')
