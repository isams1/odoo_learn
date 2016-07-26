# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report_xls'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/course_security.xml' ,
        'security/ir.model.access.csv',
        'openacademy.xml',
        'partner.xml',
        'wizard.xml',
        'report.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
