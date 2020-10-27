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
            #if self.date_order:
            #    strfecha=self.date_order[0:10]
            #else:
            strfecha=date.today()
            paridades=self.env["res.currency.rate"].search([('currency_id','=',self.moneda_adic.id)])
            for i in paridades:
                if i.name:
                    if i.name==strfecha:
                        tasacambio=i.inverse_rate
                    else:
                        tasacambio =1
            self.tasa_cambio=tasacambio

class NewModule(models.Model):
    _inherit = 'sale.order'

    subtotal_moneda_local = fields.Integer(
        string='Subtotal Moneda Local',
        required=False)

    @api.onchange('order_line','tasa_cambio')
    def _onchange_subtotal_local(self):
        return self.subtotal_moneda_local=self.amount_untaxed*self.tasa_cambio
