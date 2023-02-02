# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Challenge(models.Model):
     _name = 'blooming.challenge'
     name = fields.Char()

     challenge_id = fields.Integer(required=True)
     start_date = fields.Date()
     end_date = fields.Date()
     description = fields.Char(string="Challenge description", required=True, help="Description of the challenge")
     creator=fields.Many2one('blooming.client', string="Creator")
     participants=fields.Many2many("blooming.client", string="User")