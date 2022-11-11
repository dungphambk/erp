# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Clean Backend Theme V16',
    'version': '16.0.0.0.0',
    'sequence': 1,
    'summary': """
        Clean Backend Theme V16
    """,
    'category': 'Themes/Backend',
    'description': 'Theme',
    'author': 'Dx Deace',
    'maintainer': 'Dx Deace',
    'website': '',
    'license': 'LGPL-3',
    'price': '19.9',
    'currency': 'USD',
    'images': [
        'static/description/ss_sidebar.png'
    ],
    'depends': ['base', 'web', 'mail'],
    'data': [
        'views/webclient.xml',
        'views/icons.xml',
        'views/res_company_views.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'clean_backend_theme/static/src/scss/login.scss',
        ],
        'web._assets_primary_variables': [
            ('prepend', 'clean_backend_theme/static/src/scss/variable.scss')
        ],
        'web.assets_backend': [
            'clean_backend_theme/static/src/scss/sidebar.scss',
            'clean_backend_theme/static/src/scss/style.scss',
            'clean_backend_theme/static/src/js/sidebar.js',
            'clean_backend_theme/static/src/xml/nav_bar.xml',
        ],
    },
    'demo': [],
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False
}
