# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class Challenge(models.Model):
    _name = 'blooming.challenge'
    name = fields.Char()

    challenge_id = fields.Integer(required=True)
    start_date = fields.Date()
    end_date = fields.Date()
    description = fields.Char(string="Challenge description", required=True, help="Description of the challenge")
    creator = fields.Many2one('blooming.client', string="Creator")