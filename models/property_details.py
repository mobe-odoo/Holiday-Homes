# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields

class PropeertyDetails(models.Model):
    _name="property.details"
    _description="Details of all the properties"

    name=fields.Char('Name', required=True, placeholder="Enter property Name")
    status=fields.Selection(string="Status",selection=[('new','New'),('offer_received','Offer received'),('offer_accepted','Offer accepted'),('sold','Sold'),('canceled','Canceled')],default='new',required=True)
    country=fields.Many2one('res.country', string='Country', required=True)
    state=fields.Many2one('res.country.state', string='State', required=True)
    pincode=fields.Integer('Pin code', required=True)
    bedrooms=fields.Integer('No. of bedroom:', default=2)
    customers=fields.Many2one('res.partner', string="Customers")
    swimming_pool=fields.Boolean('Swimming Pool')
    rent=fields.Float('Rent', required=True)
    booking_ids=fields.One2many('property.booking','booking_id', string="Booking")
    