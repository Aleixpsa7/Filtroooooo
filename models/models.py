# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hremployee(models.Model):
    _inherit = 'hr.employee'

class hrdepartment(models.Model):
    _inherit = 'hr.department'

class respartner(models.Model):
    _inherit = 'res.partner'
    user_id = fields.Many2one('res.partner', string='Sales', domain=[('hrdepartment.name','=', 'Sales')])
