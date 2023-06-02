# -*- coding: utf-8 -*-
{
    'name': "Quality Check",

    'summary': """
        Quality Check""",

    'description': """
        Quality Check
    """,

    'author': "Dung Pham",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing/Quality Check',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'mrp', 'mrp_operation_package'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_quality_check_views.xml',
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
