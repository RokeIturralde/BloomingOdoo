# -*- coding: utf-8 -*-
{
    'name': "Blooming",

    'summary': """
        Share your favourite pictures with your friends""",

    'description': """
        From the cloud to your mind.
    """,

    'author': "NERD S.L.",
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
        'views/templates.xml',
            ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}