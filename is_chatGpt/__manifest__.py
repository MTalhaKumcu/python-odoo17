# -*- coding: utf-8 -*-


{
    'name': 'Odoo mtkcloud ChatGPT module',
    'version': '0.0.1',
    'license': 'AGPL-3',
    'summary': 'Odoo 17 ChatGPT Integration Module',
    'description': 'Allows the application to leverage the capabilities of the GPT language model to generate human-like responses, providing a more natural and intuitive user experience',
    'author': 'Mehmet Talha Kumcu',
    'website': 'https://www.linkedin.com/in/mehmet-talha-kumcu-6526a3209/?locale=en_US',
    'depends': ['base',],
    'category': 'Uncategorized',
    'data': [
        'security/ir.model.access.csv',
        'views/chatGPTview.xml',
    ],
    'external_dependencies': {'python': ['openai']},
    'installable': True,
    'application': True,
    'auto_install': False,

}