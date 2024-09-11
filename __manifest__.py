# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Natcom Add Saudi in arabic Field',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'summary': 'Debit Notes',
    'description': """
        Add Saudi in Arabic Field
    """,
    'depends': ['account','arabic_numbers'],
    'data': [
        'views/account.xml',
    ],
    'installable': True,
    'auto_install': False,
}
