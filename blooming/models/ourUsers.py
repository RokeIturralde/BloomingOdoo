from odoo import api
from odoo import fields
from odoo import models

class OurUsers(models.Model):
    _inherit = 'res.users'
    
    sharedAlbums = fields.Many2many("blooming.album",
                                    string="SharedAlbums")
    createdAlbums = fields.Many2one("blooming.album", "album_id",
                                    string="CreatedAlbums")