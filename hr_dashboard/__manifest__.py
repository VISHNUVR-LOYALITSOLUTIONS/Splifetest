# -*- coding: utf-8 -*-
{
    'name': "hr_dashboard",

    'summary': """
        Dashboard For HR managers and Officers.
        """,

    'description': """
        Dashboard which includes employee details, total worked hours charts, payroll analysis,
        menus and count of approvals needed and logged in user details
    """,

    'author': "Loyal IT Solutions Pvt. Ltd.",
    'website': "http://www.loyalitsolutions.com",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'hr',
        'hr_expense',
        'hr_attendance',
        'hr_holidays',
        'hr_payroll',
        'hr_recruitment',
        'hr_timesheet',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_dashboard.xml',
    ],
    'qweb': [
        "static/src/xml/hr_dashboard.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
