# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields

class HolidayHomesUsers(models.Model):
    _name="holiday_homes_users"
    _description="model to store the users"

    name=fields.Char('Name', required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "A User with the same name already exists."),
    ]