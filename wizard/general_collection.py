#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class GeneralCollectionReportWizard(models.TransientModel):
    _name = 'general.collection.report.wizard'
    _description = 'Wizard Para Cobranza General'

    partner_ids = fields.Many2many(
        'res.partner',
        # 'partner_id',
        string="Clientes",
        domain=[
            ('customer', '=', True),
            ('invoices_ids.state', '=', 'open')
        ],
        help="Seleccione una Lista de Cliente"
    )

    @api.multi
    def get_report(self):
        if len(self.partner_ids) > 0:
            try:
                report = self.env['ir.actions.report']._get_report_from_name(
                    'report_general_collection.report_general_collection'
                )
                return report.report_action(docids=self)
            except ValidationError:
                "Disculple Hubo un Error al Intenter Imprimir el Reporte",
                "Intentelo de Nuevo, y si el Problema persiste, ",
                "Contacte a su Proveedor de Servicios."
            
        else:
            raise ValidationError(
                """Disculpe debe Seleccionar por lo menos
                un Cliente para Poder Generar el Reporte"""    
            )

