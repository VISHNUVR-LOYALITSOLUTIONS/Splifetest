# -*- coding: utf-8 -*-

from odoo import models, fields, api

class projectLine(models.Model):
    _inherit = 'project.project'


    rate_per_shift = fields.Float(string="Rate Per Shift")

class Hrwork_entry_type(models.Model):
    _inherit = 'hr.work.entry.type'

    no_of_shift = fields.Float(string="No of Shifts Per day requested")

