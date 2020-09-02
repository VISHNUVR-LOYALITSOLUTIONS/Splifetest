# -*- coding: utf-8 -*-
{
    'name': "payroll_number_of_shift",

    'summary': """
        Add extra field in Payslip for No of shift""",

    'description': """
        Add extra field in Payslip for No of shift
    """,

    'author': "Loyal IT Solutions Pvt. Ltd.",
    'website': "http://www.loyalitsolutions.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_payroll','hr_work_entry'],

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
