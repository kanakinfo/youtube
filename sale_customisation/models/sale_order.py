# -*- coding: utf-8 -*-

from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('name', 'partner_id.name')
    def _compute_display_name(self):
        for order in self:
            order.display_name = f"{order.name}({order.partner_id.name})"
