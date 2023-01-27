# -*- coding: utf-8 -*-
{
    'name': "Blooming",

    'summary': """
        Module of our application Blooming""",

    'description': """
        This app is able to create albums for the children
    """,

    'author': "NERD S.L",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/membershipPlan.xml',
        'views/content.xml',
        'views/ContentViews.xml',
        'views/templates.xml',
        "views/clientViews.xml",
            ],
    # only loaded in demonstration mode
    'demo': [
        'demo/content.xml',
    ],
}