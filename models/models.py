# -*- coding: utf-8 -*-

from odoo import models, fields, api

class filtro(models.Model):
    _name: 'res.partner'
    sales_id = fields.Many2one('res.partner', string='Sales', domain=[('department_id.name','=', 'Sales')])