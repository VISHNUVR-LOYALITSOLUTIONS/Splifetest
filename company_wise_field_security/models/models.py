# -*- coding: utf-8 -*-

from odoo import models, fields, api


class company_wise_field_security(models.Model):
    _inherit = 'res.company'

    senior_living = fields.Boolean(string="Senior Living",default=False)
    ayurlaya_name = fields.Boolean(string="Ayurlaya",default=False)
    fhc_name = fields.Boolean(string="FHC",default=False)
    home_nursing_name = fields.Boolean(string="Home Nursing",default=False)


class Respartner(models.Model):
    _inherit = 'res.partner'

    x_senior_living = fields.Boolean(string="Senior Living",default=False,compute='_compute_senior_security')
    x_ayurlaya_name = fields.Boolean(string="Ayurlaya",default=False,compute='_compute_ayurlaya_security')
    x_fhc_name = fields.Boolean(string="FHC",default=False,compute='_compute_fhc_security')
    x_home_nursing_name = fields.Boolean(string="Home Nursing",default=False,compute='_compute_home_nursing_security')



    @api.depends('company_id')
    def _compute_senior_security(self):
        company = self.env.user.company_id
        company_val = self.env.company.id
        for i in self:
            if i.env.company.senior_living==True:
                i.x_senior_living = True

            else:
                i.x_senior_living = False

    @api.depends('company_id')
    def _compute_ayurlaya_security(self):
        company = self.env.user.company_id
        company_val = self.env.company.id
        for i in self:

            if i.env.company.ayurlaya_name == True:
                i.x_ayurlaya_name = True

            else:
                i.x_ayurlaya_name = False
    @api.depends('company_id')
    def _compute_fhc_security(self):
        company = self.env.user.company_id
        company_val = self.env.company.id
        for i in self:

            if i.env.company.fhc_name==True:
                i.x_fhc_name = True

            else:
                i.x_fhc_name =False
    @api.depends('company_id')
    def _compute_home_nursing_security(self):
        company = self.env.user.company_id
        company_val = self.env.company.id
        for i in self:

            if i.env.company.home_nursing_name==True:
                i.x_home_nursing_name = True
            else:
                i.x_home_nursing_name = False


    #
    #
