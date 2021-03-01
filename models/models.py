# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hremployee(models.Model):
    _inherit = 'hr.employee'
    department_id = fields.Many2one('hr.department', 'Department')

class respartner(models.Model):
    _inherit = 'res.partner'
    sales_id = fields.Many2one('res.partner', string='Sales', domain=[('department_id','=', 'Sales')])
