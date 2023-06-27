# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Motorcycle Registry",
    "version": "1",
    "category": "Kawiil",
    'icon': '/motorcycle_registry/static/img/icon.png',
    "summary": "Manage Registration of Motorcycles",
    "description": """Motorcycle Registry
====================
This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.""",
    "author": "yavy-odoo",
    "website": "https://github.com/yavy-odoo/",
    "depends": [
        "base",
    ],
    "data": [
        "demo/motorcycle_demo.xml",
        # "views/templates.xml",
    ],
    "assets": [],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True
}
