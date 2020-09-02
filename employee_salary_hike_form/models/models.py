# -*- coding: utf-8 -*-

from odoo import models, fields, api



class salary_hike_form(models.Model):
    _name = 'salary.hike.form'
    _description = 'Salary Hike Form'


    order_line = fields.One2many('salary.hike.form.line', 'order_id', string='Recruitment Form')

    employee_name = fields.Many2one('hr.employee',string='Employee Name',store=True)





class Recruitment_questions_form_line(models.Model):
    _name = 'salary.hike.form.line'




    order_id = fields.Many2one('salary.hike.form', string='Salary Hike', ondelete='cascade')

    entering_date = fields.Date(string='Date Of Interview', store=True, default=fields.Date.context_today)


    current_salary = fields.Float(string="Current Salary",store=True)
    increment_amount = fields.Float(string="Increment Amount",store=True)


    employee_name = fields.Many2one('hr.employee', string='Employee Name', store=True,related='order_id.employee_name')

    @api.onchange('order_id','entering_date','employee_name')
    def _onchange_employee_name(self):
        for i in self:
            contracts = i.order_id.employee_name.contract_ids
            for j in contracts:
                if j.date_end != False:
                    if i.entering_date >= j.date_start and i.entering_date <= j.date_end:
                        i.current_salary = j.hourly_wage
                else:
                    if i.entering_date >= j.date_start and j.date_end==False:
                        i.current_salary = j.hourly_wage

                # else:
                #     if i.entering_date >= j.date_start:
                #         i.current_salary = j.hourly_wage
                #     else:
                #         i.current_salary = 0.00




class Hrapplicannt_questions(models.Model):
    _inherit = 'hr.employee'


    def salary_hike_window(self, context=None):
        dom = self.env['salary.hike.form'].search(

            [('employee_name', '=', self.id)]).ids

        domain = [('id', 'in', dom)]

        form_view_id = self.env.ref('employee_salary_hike_form.salary_hike_line_setup_form').id

        view_id = self.env.ref('employee_salary_hike_form.salary_hike_line_tree').id
        # recruitment_questions_line_tree
        return {
            'name': 'Salary Hike Form',
            'view_type': 'form',
            'view_mode': 'tree',
            'res_model': 'salary.hike.form',
            'views': [[view_id, 'tree'], [form_view_id, 'form']],
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            # 'target': 'new',
            # 'context': {},

            # 'views': [(view.id, 'form')],
            # 'context': self.env.context,
            # 'res_id': self.id,
            'domain': domain
        }

