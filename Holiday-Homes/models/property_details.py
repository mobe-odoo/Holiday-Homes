# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,models,fields
from datetime import date

class PropeertyDetails(models.Model):
    _name="property.details"
    _description="Details of all the properties"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name=fields.Char('Name', required=True, placeholder="Enter property Name")
    description=fields.Text('Description')
    address=fields.Text('Address', required=True)
    status=fields.Selection(string="Status",selection=[('available','Available'),('on_rent','On rent')],default='available', tracking=True)
    country=fields.Many2one('res.country', string='Country', required=True)
    state=fields.Many2one('res.country.state', string='State', required=True)
    image = fields.Image(string='Image', attachment=True,store=True)
    pincode=fields.Integer('Pin code', required=True)
    bedrooms=fields.Integer('No. of bedroom:', default=2)
    property_area=fields.Integer('Property area sq.ft')
    available_from=fields.Date('Available from:' ,default=date.today(), compute="_compute_available_date")
    customers=fields.Many2one('res.partner', string="Customers")
    swimming_pool=fields.Boolean('Swimming Pool')
    rent_amount=fields.Float('Rent amount', required=True)
    booking_ids=fields.One2many('property.booking','booking_id', string="Booking")
    
    @api.depends('booking_ids')
    def _compute_available_date(self):
        latest_rec = self.env['property.booking'].search([], limit=1, order='check_out desc')
        for record in self:
            record.available_from = latest_rec.check_out
       