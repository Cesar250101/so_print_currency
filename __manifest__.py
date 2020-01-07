# -*- coding: utf-8 -*-
{
    'name': "so_print_currency",

    'summary': """
        Extanción para poder imprimir notas de venta en una moneda extranjera""",

    'description': """
        Imprimir notas de venta en la moneda extranajera seleccionada
    """,

    'author': "Method",
    'website': "http://www.openmethod.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/sale_order.xml',
        'reports/sale_order_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}