# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class Album(models.Model):
    _name = 'blooming.album'
    
    #Attributes
    album_id = fields.Integer()
    name = fields.Char()
    description = fields.Text()
    #creator = fields.ManyToOne('res.users', string="Creator")
    #users = fields.Many2Many('res.users', string="Users")
    creationDate = fields.Date()
    #contents = fields.Many2Many('blooming.content', string="Contents")
