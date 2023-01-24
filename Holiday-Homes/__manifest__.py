# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Holiday Homes',
    'version' : '1.0',
    'depends' : ['mail'],
    'author' : 'mobe',
    'data' : [
        'security/ir.model.access.csv',
        'views/holiday_homes_menus.xml',
        'views/property_details_views.xml',
        'views/property_booking_views.xml',
        'views/holiday_homes_users_views.xml',
      
    ],
    'demo' : [
        # 'demo/property_details_demo.xml',
    ],
    'application' : True,
    'installable' : True,
    'auto-install' : False,

}