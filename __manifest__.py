# -*- coding: utf-8 -*-
{
    'name': "tutorial Odoo",

    'summary': """
        this module is a litle practique if you want to know more..
        I follow this tutorial https://www.odoo.com/documentation/14.0/developer/""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Wendry Koralis",
    'website': "https://www.linkedin.com/in/wendry-koralis-poueriet-mart%C3%ADnez-a68bba1b4/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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
