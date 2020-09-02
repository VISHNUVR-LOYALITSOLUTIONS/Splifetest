# -*- coding: utf-8 -*-
{
    'name': "hr_payroll_account_operating_unit",

    'summary': """
        HR Payroll Account Operating Unit""",

    'description': """
        HR Payroll Account Operating Unit
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',"hr_payroll_account",
        "hr_contract_operating_unit",
        "account_operating_unit",],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
