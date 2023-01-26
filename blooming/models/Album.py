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
    creator = fields.Many2One('res.users', string="Creator", required=True)
    users = fields.Many2Many('res.users', string="Users")
    creationDate = fields.Date(string="Creation Date")
    contents = fields.Many2Many('blooming.content', string="Contents")
