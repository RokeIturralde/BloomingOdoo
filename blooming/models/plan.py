# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class Plan(models.Model):
    _name = 'blooming.plan'
    name = fields.Char()
    albumLimit = fields.Integer()
    description = fields.Char()
    duration = fields.Char()
    price = fields.Float()
    shareable = fields.Boolean()
