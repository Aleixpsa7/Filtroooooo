# -*- coding: utf-8 -*-

from odoo import models, fields, api

class filtro(models.Model):
    _name: 'filtro.sales'
    _inherits = ['res.partner','hr.employee', 'hr.department']
    sales_id = fields.Many2one('res.partner', string='Sales', domain=[('department_id.name','=', 'Sales')])