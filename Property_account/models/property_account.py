# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,Command

class PropertyDetails(models.Model):
    _inherit="property.details"

    def action_confirm(self):
        for record in self:
            self.env["account.move"].create(
                {
                    "partner_id" : record.buyer_id.id,
                    "move_type" : "out_invoice",
                    # "line_ids" : [
                    #     Command.create(
                    #         {
                    #             "name" : record.name,
                    #             "quantity" : 1.0,
                    #             "price_unit" : 
                    #         }
                    #     )
                    # ]
                }
            )
        return super().action_confirm()