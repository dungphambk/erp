# -*- coding: utf-8 -*-
{
    'name': "Production Line",

    'summary': """
        Production Line""",

    'description': """
        Production Line
    """,

    'author': "Dung Pham",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing/Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp', 'mrp_operation_package'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_production_line_views.xml',
        'views/mrp_production_log_views.xml',
        'views/mrp_manufacturing_form_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
