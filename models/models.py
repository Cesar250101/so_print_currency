# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date, time, timedelta

class ImprimirNotaVenta(models.Model):
    _inherit = 'sale.order'

    imprimir_moneda_extranjera = fields.Boolean(string="Imprimir en moneda extranjera",  )
    moneda_adic = fields.Many2one(comodel_name="res.currency", string="Moneda Adicional", required=False, default=46)
    tasa_cambio = fields.Float(string="Tasa de Cambio",  required=False, store=True)

    @api.model
    @api.onchange('moneda_adic')
    def _onchange_moneda_Adic(self):
        if self.tasa_cambio in(1,0):
            tasacambio=1
            strfecha=self.date_order[0:10]
            paridades=self.env["res.currency.rate"].search([('currency_id','=',self.moneda_adic.id)])
            for i in paridades:
                if i.name==strfecha:
                    tasacambio=i.inverse_rate
            self.tasa_cambio=tasacambio

