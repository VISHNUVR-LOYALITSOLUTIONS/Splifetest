# -*- coding: utf-8 -*-
{
    'name': "department_wise_restriction",

    'summary': """
       Department wise Restriction for
       1.employee
       2.Contract
       3.Payroll
       4.Work entry
       5 Work entry type """,

    'description': """
         Department wise Restriction for
       1.employee
       2.Contract
       3.Payroll
       4.Work entry
       5 Work entry type
       
       user->department
    """,

    'author': "Loyal IT Solutions Pvt. Ltd.",
    'website': "http://www.loyalitsolutions.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_work_entry','hr_payroll'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
