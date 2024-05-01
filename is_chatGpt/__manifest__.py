# -*- coding: utf-8 -*-
{
    'name': "My Odoo ChatGPT Module",
    'summary': "This module integrates ChatGPT into Odoo 17.",
    'description': """
        This module integrates ChatGPT into Odoo 17, allowing users to generate text using GPT-3.5 API.
    """,
    'author': "Mehmet Talha Kumcu",
    'website': "https://www.google.com",
    'category': 'UncSategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/gpt_views.xml',
    ],
   # 'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
