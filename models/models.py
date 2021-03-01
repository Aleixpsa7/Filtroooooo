# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hremployee(models.Model):
    _inherit = 'hr.employee'
    department_id = fields.Many2one('hr.department', 'Department')

<<<<<<< HEAD
class respartner2(models.Model):
    sales_id = fields.Many2one('res.partner', string='Sales', domain=[('department_id','=', 'Sales')])
=======
class respartner(models.Model):
    _inherit = 'res.partner'
    sales_id = fields.Many2one('res.partner', string='Sales', domain=[('department_id.user_id','in', 'Sales' )])
>>>>>>> 107691fe38750608bac11806b9bc625d06ce26fe
