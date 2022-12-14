# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Estate_property(models.Model):
    _name = 'estate.property'
    _description = 'Estate property'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([('n','North'),('s','South'),('e','East'),('w','West')])
