# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Recruitment_questions(models.Model):
    _name = 'recruitment.questions'
    _description = 'Recruitment Questions'

    name = fields.Char(string="Questions")


class Recruitment_questions_form(models.Model):
    _name = 'recruitment.questions.form'
    _description = 'Recruitment Form'

    overall_option_ids = fields.One2many(
        'overall.option', 'order_id', 'Overall Option',
        )

    order_line = fields.One2many('recruitment.questions.form.line', 'order_id', string='Recruitment Form')

    candidate_name = fields.Many2one('hr.applicant',string='Candidate Name',store=True)

    entering_date = fields.Date(string='Date Of Interview', store=True, default=fields.Date.context_today)

    position = fields.Many2one('hr.department',string="Position")
    employee_name = fields.Many2one('hr.employee', string="Interviewer")



class Recruitment_questions_form_line(models.Model):
    _name = 'recruitment.questions.form.line'

    display_type = fields.Selection([
        ('line_section', 'Section'),
        ('line_note', 'Note'),
    ], default=False, help="Technical field for UX purpose.")



    sale_order_option_ids = fields.One2many('overall.option', 'line_id', 'Optional Products Lines')


    order_id = fields.Many2one('recruitment.questions.form', string='Room Chart', ondelete='cascade')

    recruitment_quest= fields.Many2one('recruitment.questions', string="Questions", store=True)
    exceptionnal_bool = fields.Boolean(string="5",default=False)
    above_average_bool = fields.Boolean(string="4",default=False)
    average_bool = fields.Boolean(string="3", default=False)
    satisfactory_bool = fields.Boolean(string="2", default=False)
    unsatisfactory_bool = fields.Boolean(string="1", default=False)

class overallOrderOption(models.Model):
    _name = "overall.option"

    display_type = fields.Selection([
        ('line_section', 'Section'),
        ('line_note', 'Note'),
    ], default=False, help="Technical field for UX purpose.")

    order_id = fields.Many2one('recruitment.questions.form', 'Overall Reference', ondelete='cascade')
    line_id = fields.Many2one('recruitment.questions.form.line', ondelete="set null", )
    name = fields.Text('Description', required=True)
    advance_bool = fields.Boolean(string="Advance", default=False)
    advance_res_bool = fields.Boolean(string="Advance With reservations", default=False)
    dont_advance_bool = fields.Boolean(string="Do not advance", default=False)


class Hrapplicannt_questions(models.Model):
    _inherit = 'hr.applicant'

    # order_id = fields.Many2one('recruitment.questions.form', string='Room Chart', ondelete='cascade')


    def name_get(self):
        res = []
        for field in self:
            res.append((field.id, '%s-(%s)' % (field.name, (field.partner_name))))
        return res

    def action_questions_value(self):



        # action = self.env.ref('recruitment_questions_form.recruitment_questions_line_setup_form').read()[0]
        #
        # form_view = [(self.env.ref('stock.view_picking_form').id, 'form')]
        #
        # action['views'] = form_view
        # action['res_id'] = self.env.ref('recruitment_questions_form.recruitment_questions_line_setup_form').id
        #
        # return action

        #
        view_id = self.env.ref('recruitment_questions_form.recruitment_questions_line_setup_form').id


        return {
            'name':'Recruitment Form',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'recruitment.questions.form',
            'view_id':view_id,
            'type':'ir.actions.act_window',
            'target':'new',
            'context': {},
        }

    def tree_view_action_questions_value(self,context=None):


        dom = self.env['recruitment.questions.form'].search(

            [('candidate_name', '=', self.id)]).ids

        domain = [('id', 'in', dom)]


        form_view_id = self.env.ref('recruitment_questions_form.recruitment_questions_line_setup_form').id


        view_id = self.env.ref('recruitment_questions_form.recruitment_questions_line_tree').id
        # recruitment_questions_line_tree
        return {
            'name': 'Recruitment Form',
            'view_type': 'form',
            'view_mode': 'tree',
            'res_model': 'recruitment.questions.form',
            'views': [[view_id, 'tree'], [form_view_id, 'form']],
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            # 'target': 'new',
            # 'context': {},

            # 'views': [(view.id, 'form')],
            'context': self.env.context,
            'res_id': self.id,
            'domain':domain
        }



