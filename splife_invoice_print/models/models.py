# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from num2words import num2words

from num2words import num2words

class Hremployee(models.Model):
    _inherit = 'hr.employee'

    acc_number = fields.Char(string="A/C No.")