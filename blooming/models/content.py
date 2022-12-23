# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class Content(models.Model):
    _name = 'blooming.content'
    contentId = fields.Integer()
    name = fields.Char()
    uploadDate = fields.Date()
    albums = fields.Many2many("blooming.album",
                              string="Albums")
                              
class CustomImage(models.Model):
    _inherit = 'blooming.content'
    image = fields.binary(help="Select image here")
    
class CustomText(models.Model):
    _inherit = 'blooming.content'
    text = fields.Char()
 
 