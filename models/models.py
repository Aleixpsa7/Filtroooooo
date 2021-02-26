# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hrdepartment(models.Model):
    _inherit = 'hr.department'
    user_id = fields.Many2one('hr.department', string='Sales', index=True, track_visibility='onchange', default=lambda self: self.env.user)