# -*- coding: utf-8 -*-
{
    'name': "work_entry_approval_stage",

    'summary': """
        1.Approval button in work entry with 'Validate Approval' state.
        2.payslip lines according to the 'Validate Approval' state in work entry and cancel the draft state work entry.
        """,

    'description': """
       1.Approval button in work entry with 'Validate Approval' state.
        2.payslip lines according to the 'Validate Approval' state in work entry and cancel the draft state work entry.
    """,

    'author': "Loyal IT Solutions Pvt. Ltd.",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_work_entry','hr_contract','hr_payroll'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/approval_security.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/action_window.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
