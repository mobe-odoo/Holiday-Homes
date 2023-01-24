# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,models,fields
from dateutil.relativedelta import relativedelta
from datetime import date,datetime
from odoo.exceptions import UserError, ValidationError

class PropertyBooking(models.Model):
    _name="property.booking"
    _description="Model for booking property on rent"

    name_id=fields.Many2one('res.partner', string="Name")
    email=fields.Char(related="name_id.email",string='E-mail', required=True)
    phone=fields.Char(related="name_id.phone",string='Phone No.', required=True)
    address=fields.Char(related="name_id.street",string='Permanent Address')
    age=fields.Integer('Age')
    members=fields.Integer('Total members', required=True)
    check_in=fields.Date('CHECK-IN', required=True,default=date.today())
    check_out=fields.Date('CHECK-OUT', required=True,default=date.today())
    total_days=fields.Integer('Days', compute="_compute_total_days")
    total_amount=fields.Float('Total amount', compute="_compute_total_amount")
    buyer_id=fields.Many2one('res.partner', copy=False, string="user")
    booking_id=fields.Many2one('property.details')


    @api.depends('check_in', 'check_out')
    def _compute_total_days(self):
        for record in self:
            record.total_days=(record.check_out - record.check_in).days

    @api.depends('booking_id', 'total_days')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount=(record.total_days * record.booking_id.rent_amount)

    @api.constrains('check_in', 'check_out')
    def _check_date_validation(self):
        for record in self:
            if record.total_days<0:
                raise ValidationError("Check-out date cannot be previous than check-in date!!")
    
    
    @api.model
    def create(self,vals):
        booking_id=self.env['property.details'].browse(vals['booking_id'])
        latest_rec = self.env['property.booking'].search([], limit=1, order='check_out desc')
        if booking_id.available_from:
            if datetime.strptime(vals['check_in'] , '%Y-%m-%d').date() < booking_id.available_from:
                raise UserError(("Check-In date cannot be less than the availability"))
        return super().create(vals)

