# -*- coding: utf-8 -*-
from odoo import models, fields, api
# Import logger
# -*- coding: utf-8 -*-
from odoo import models, fields, api
# Import logger
import logging

# Get the logger
_logger = logging.getLogger(__name__)

# External import
from datetime import datetime, date, timedelta


class scheduler_demo(models.Model):
    _name = 'scheduler.demo'

    name = fields.Char(required=True)
    numberOfUpdates = fields.Integer('Number of updates', help='The number of times the scheduler has run and updated '
                                                               'this field')
    lastModified = fields.Date('Last updated')

    # This function is called when the scheduler goes off
    def process_demo_scheduler_queue(self):

        # scheduler_line_obj = self.pool.get('scheduler.demo')
        scheduler_line_obj = self.env['scheduler.demo']

        # scheduler_line_ids = self.pool.get('scheduler.demo').search(cr, uid, [])
        scheduler_line_ids = self.env['scheduler.demo'].search([])

        for scheduler_line_id in scheduler_line_ids:

            scheduler_line = scheduler_line_obj.browse(scheduler_line_id.id)
            numberOfUpdates = scheduler_line.numberOfUpdates

            aux = datetime.strptime(scheduler_line.lastModified, '%Y-%m-%d')
            resta = aux.date() - datetime.now().date()
            if (resta.days >= -2 and resta.days <= 0):
                print ("Hola")
            _logger.info('line: ' + scheduler_line.name)
            _logger.info('numberOfUpdates: ' + str(scheduler_line.numberOfUpdates))

            scheduler_line_id.write(
                {'numberOfUpdates': (numberOfUpdates + 1), 'lastModified': str(datetime.now().date())})

	    
