# -*- coding: utf-8 -*-
{
    'name': "Odoo-Actions",

    'summary': """
        This demo will show you how to create a new scheduler that automatically runs
	and will update all records in the current model.""",

    'description': """
        This demo will show you how to create a new scheduler that automatically runs
	and will update all records in the current model. Every time the scheduler is run it will 
        update all records on this model and will update the 'Number of updates' as demo.
    """,

    'author': "Andyeyo",
    'version': '0.1',
    'depends': ['base','web_notify'],
    'data': [
	'data/default_data.xml',
	'data/scheduler_data.xml',
	'views/scheduler_view.xml'
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
