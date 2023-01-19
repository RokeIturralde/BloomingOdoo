# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class Album(models.Model):
    _name = 'blooming.album'
    
    #Attributes
    album_id = fields.Integer(string="Id")
    name = fields.Char(string="Name", required=True, help="Name of the album")
    description = fields.Text(string="Description")
    creator = fields.Many2One('res.users', string="Creator", required=True, help="Login of the Album creator")
    users = fields.Many2Many('res.users', string="Users")
    creationDate = fields.Date()
    contents = fields.Many2Many('blooming.content', string="Contents")
