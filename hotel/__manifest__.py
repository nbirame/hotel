# -*- coding: utf-8 -*-
{
    'name': "Hotel",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    "version": "13.0.1",

    # any module necessary for this one to work correctly
    'depends': ['base',"web",'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        #'views/templates.xml',
        'data/menu.xml',
        'views/chambre_views.xml',
        'views/location_views.xml',
        'views/template_chambre_view.xml',
        #'views/template_detail',
        'views/templates2.xml',
        'data/hotel_sequence.xml',
    ],
    #  only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    "installable": True,
    #'images': ['static/description/banner.png'],
    "auto_install": False,
    "application": False,
    "license": "AGPL-3",
}