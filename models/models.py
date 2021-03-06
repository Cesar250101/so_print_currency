# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date, time, timedelta

class ImprimirNotaVenta(models.Model):
    _inherit = 'sale.order'

    imprimir_moneda_extranjera = fields.Boolean(string="Imprimir en moneda extranjera",  )
    moneda_adic = fields.Many2one(comodel_name="res.currency", string="Moneda Adicional", required=False, default=46)
    tasa_cambio = fields.Float(string="Tasa de Cambio", related="moneda_adic.inverse_rate" ,required=False, store=True)


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

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    price_unit = fields.Float(
        string='Precio Unitario',
        required=False)

    precio_moneda_adicional = fields.Float(
        string='Precio Moneda Adicional',relate="product_id.product_tmpl_id.lst_price",
        required=False)
    tasa_cambio_linea = fields.Float(string="Tasa de Cambio", required=False, store=True, related="order_id.tasa_cambio")



    @api.onchange('precio_moneda_adicional','product_uom_qty')
    def _onchange_price_unit(self):
        if self.order_id.tasa_cambio!=1:
            self.price_unit=self.precio_moneda_adicional*self.order_id.tasa_cambio

