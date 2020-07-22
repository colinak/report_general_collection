#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Report General Collection",
    "version": "12.0.1.1.0",
    "category": "Accounting Invoicing",
    "website": "https://github.com/colinak",
    "author": "Kewitz Colina",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "depends": [
        'base',
        'account'
    ],
    "data": [
        'report/report_general_collection.xml',
        'wizard/general_collection_wizard.xml',
    ],
    "demo": [
    ],
}
