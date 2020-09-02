# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError, ValidationError




class Room_Floor(models.Model):
    _name = 'room.floor'
    _description = 'Floors'

    name = fields.Char(string="Room Name")


class Room_Flat(models.Model):
    _name = 'room.flat'
    _description = 'Flats'

    name = fields.Char(string="Flat Name")

class Room_Occupy_type(models.Model):
    _name = 'room.occupy'
    _description = 'Room Occupancy type'

    name = fields.Char(string="Room Type")

class Room_Type(models.Model):
    _name = 'room.type'
    _description = 'Room type'

    name = fields.Char(string="Type")


class Room_room(models.Model):
    _name = 'room.room'
    _description = 'Rooms'

    name = fields.Char(string="Name")
    floor_name = fields.Many2one('room.floor', string="Floor")
    flat_name = fields.Many2one('room.flat', string="Flat")
    occupy_type = fields.Many2one('room.occupy', string="Occupy Type")
    # room_type = fields.Many2one('room.type', string="Living Type")

    status = fields.Selection([
        ('vacant', 'Vacant'),
        ('occupy', 'Occupy'),
    ], default="vacant", store=True, )



    @api.constrains('name')
    def _check_unique_name(self):
        for line in self:
            if line.name:
                if len(self.search([('name', '=', line.name)])) > 1:
                    raise ValidationError("Name Already Exists")
            else:
                pass


class Room_chart_management(models.Model):
    _name = 'room.chart'


    order_line = fields.One2many('room.chart.line', 'order_id', string='Room Chart Lines')

    name = fields.Char(string='Reference', readonly=True,store=True,default=lambda self: _('New'))

    entering_date = fields.Date(string='Order Date',store=True, default=fields.Date.context_today)

    occupant_name = fields.Many2one('res.partner',string="Occupant Name")

    current_status = fields.Selection([
        ('vacant', 'Vacant'),
        ('occupy', 'Occupy'),
    ], default="vacant", store=True, )

    occupy_type = fields.Many2one('room.occupy',string="Occupy Type")
    living_type = fields.Many2one('room.type', string="Living Type")

    tmp_chart_room = fields.Many2one('room.room', string="Room", store=True,related='order_line.chart_room')
    tmp_chart_floor = fields.Many2one('room.floor', string="Floor", store=True,related='order_line.chart_floor')
    tmp_chart_flat = fields.Many2one('room.flat', string="Flat", store=True,related='order_line.chart_flat')
    tmp_chart_status = fields.Selection([
        ('vacant', 'Vacant'),
        ('occupy', 'Occupy'),
    ], default="vacant", store=True, related='order_line.chart_status')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('room.chart') or '/'
        return super(Room_chart_management, self).create(vals)


    def action_confirm(self):
        self.current_status='occupy'

        for change in self.order_line:
            if change.chart_room:
                room_id = change.chart_room.id
                customer_group = self.env['room.room'].browse(room_id).write(
                    {
                        'status': change.chart_status
                    }
                )
                change.chart_room.status = change.chart_status


    def action_vacant(self):
        self.current_status = 'vacant'

        for change in self.order_line:
            if change.chart_room:
                room_id = change.chart_room.id
                customer_group = self.env['room.room'].browse(room_id).write(
                    {
                        'status': change.chart_status
                    }
                )
                change.chart_room.status = change.chart_status




class Room_chartline_management(models.Model):
    _name = 'room.chart.line'


    order_id = fields.Many2one('room.chart', string='Room Chart', ondelete='cascade')

    chart_room = fields.Many2one('room.room',string="Room",store=True)
    chart_floor = fields.Many2one('room.floor',string="Floor",store=True)
    chart_flat = fields.Many2one('room.flat',string="Flat",store=True)
    chart_status = fields.Selection([
        ('vacant', 'Vacant'),
        ('occupy', 'Occupy'),
    ], default="vacant", store=True,related='order_id.current_status')

    @api.onchange('chart_room')
    def onchange_room_get_domain(self):
        room_list = []
        roomsline_id = self.env["room.room"].search([('status', '=', 'vacant')])
        for line_id in roomsline_id:
            room_list.append(line_id.id)
        result = {'domain': {'chart_room': [('id', 'in', room_list)]}}
        return result



    @api.onchange('chart_room')
    def _onchange_room(self):
        for room in self:
            if room.chart_room:
                room.chart_floor = room.chart_room.floor_name
                room.chart_flat= room.chart_room.flat_name
                room.chart_status = room.chart_room.status









