# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hremployee(models.Model):
    _inherit = 'hr.employee'
    user_id = fields.Many2one('hr.employee', string='Sales', default=lambda self: self.env.user)

class hrdepartment(models.Model):
    _inherits = {'hr.department': 'department_id'}
    department_id = fields.Many2one('hr.department', string='Department')