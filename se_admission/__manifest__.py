# -*- coding: utf-8 -*-
{
    'name': "SmartEdu Admission",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '16.0.1',

    'depends': [
        'base',
        'contacts',
        'account',
        'mail',
        'se_education_core',
    ],

    # always loaded
    'data': [

        # security
        'security/ir.model.access.csv',

        # views
        'views/se_batch_view.xml',
        'views/se_application_views.xml',
        'views/se_application_register_view.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
