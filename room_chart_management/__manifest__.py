# -*- coding: utf-8 -*-
{
    'name': "Room chart Management",

    'summary': """
        Room chart Management""",

    'description': """
    
     Room chart Management
    
        1.Room creation
        2.Floor Creation
        3.Living Type creation
        4.Flat creation
        5.Room Chart creation
       
    """,

    'author': "Loyal IT Solutions Pvt. Ltd.",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [

       'data/ir_sequence.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/floor.xml',
       'views/room_chart.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
