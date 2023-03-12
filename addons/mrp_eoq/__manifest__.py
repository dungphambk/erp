# -*- coding: utf-8 -*-
{
    'name': "mrp_eoq",

    'summary': """
        EOQ""",

    'description': """
        Calculate EOQ
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'mrp', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/mrp_eoq.xml',
        'views/purchase_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
