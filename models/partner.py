#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_id = fields.Many2one(
        'res.partner',
        'Cliente',
    )
    invoices_ids = fields.One2many(
        'account.invoice',
        'partner_id',
        'Facturas',
        help="Seleccione las Facturas"
    )
