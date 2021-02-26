# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hremployee(models.Model):
    _inherits = {'hr.employee': 'department_id'}
    user_id = fields.Many2one('hr.employee', string='Sales', default=lambda self: self.env.user)