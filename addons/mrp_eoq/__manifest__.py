# -*- coding: utf-8 -*-
{
    'name': "Economic Order Quantity / Production Order Quantity / Discount Quantity Model",

    'summary': """
        EOQ / POQ / Discount Quantity Model""",

    'description': """
        Calculate EOQ / POQ / Discount Quantity Model
    """,

    'author': "Dung Pham",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing/Planning',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'mrp', 'purchase', 'sale', 'stock', 'mrp_planning_package'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/mrp_eoq.xml',
        'views/mrp_poq.xml',
        'views/mrp_discount.xml',
        'views/purchase_views.xml',
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
