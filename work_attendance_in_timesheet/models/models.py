# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime



class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'


    total_attendance = fields.Float("Total Attendance",default=0.0)

    hr_work_entry_ids = fields.Many2many(
        comodel_name='hr.work.entry', string='Related work Entry', readonly=True,
        copy=False,
        help="Related work Entry"
             )

    # @api.multi
    # @api.depends('picking_ids')
    # def _get_pickings(self):
    #     for lines in self:
    #
    #         picking_ids = lines.picking_ids
    #         if picking_ids:
    #             lines.del_number = ', '.join(picking_ids.mapped('name'))


class Hrprojects(models.Model):
    _inherit = 'hr.work.entry'

    total_work_attendance = fields.Float("Total Attendance", default=0.0)

    project_id = fields.Many2one('project.project', 'Project')
    project_task = fields.Many2one('project.task', 'Task')

    time_sheet_ids = fields.Many2many(
        comodel_name='account.analytic.line',
        copy=False,
        string='Time Sheet',
        readonly=True,
    )

    def action_view_work(self):

        if self.employee_id:
            if self.employee_id.user_id:
                user_id = self.employee_id.user_id.id
            else:
                user_id = self.time_sheet_ids._default_user()
        else:
            user_id = self.time_sheet_ids._default_user()
        # so_line= self.time_sheet_ids._default_sale_line_domain()

        query3 = """
        
        
        select sum(duration) as total_work_attendance,CAST(w.date_start AS DATE) from hr_work_entry as w
                    WHERE CAST(w.date_start AS DATE) =%s and w.employee_id=%s
                            group by CAST(w.date_start AS DATE)

                                                """

        self.env.cr.execute(query3, (datetime.strptime(str(self.date_start),'%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d'),self.employee_id.id))

        total_work = 0
        for ans1 in self.env.cr.dictfetchall():
            total_work= ans1['total_work_attendance'] if ans1['total_work_attendance'] else 0

        res = {

            'total_work_attendance': total_work if total_work else 0.0,
        }

        self.total_work_attendance =res['total_work_attendance']

        so_order = {
            # 'partner_id': self.partner_id.id,
            'employee_id': self.employee_id.id,
            'task_id': self.project_task.id,
            'user_id':user_id,
            'date': self.date_start,
            'project_id': self.project_id.id,
            'total_attendance': self.total_work_attendance,
            'unit_amount':self.duration,
            'name':self.name
            # 'so_line':1

        }

        so = self.env['account.analytic.line'].create(so_order)


        return

        # self.ensure_one()
        # action = self.env.ref('hr_timesheet.hr_timesheet_line_tree')
        # result = action.read()[0]
        # if len(self.time_sheet_ids) > 1:
        #     result['domain'] = "[('id', 'in', %s)]" % self.time_sheet_ids.ids
        # else:
        #
        #     form_view = self.env.ref('timesheet_grid.timesheet_view_form')
        #     result['views'] = [(form_view.id, 'form')]
        #     result['res_id'] = self.time_sheet_ids.id
        # return result








