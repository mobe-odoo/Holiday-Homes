# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields

class PropertyBooking(models.Model):
    _name="property.booking"
    _description="Model for booking property on rent"

    name_id=fields.Many2one('res.partner', string="Name")
    email=fields.Char(related="name_id.email",string='E-mail', required=True)
    phone=fields.Integer(string='Phone No.', required=True)
    address=fields.Char(related="name_id.street",string='Permanent Address')
    age=fields.Integer('Age')
    members=fields.Integer('Total members', required=True)
    check_in=fields.Date('CHECK-IN', required=True)
    check_out=fields.Date('CHECK-OUT', required=True)
    total_days=fields.Integer('Days', compute="_compute_total_days")
    total_amount=fields.Float('Total ammount', compute="_compute_total_amount")
    buyer_id=fields.Many2one('res.partner', copy=False, string="user")
    booking_id=fields.Many2one('property.details')