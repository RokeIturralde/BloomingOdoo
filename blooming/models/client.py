from odoo import api
from odoo import fields
from odoo import models

class Client(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'
    
    sharedAlbums = fields.Many2many("blooming.album",
                                    string="SharedAlbums")
    createdAlbums = fields.Many2one("blooming.album", "album_id",
                                    string="CreatedAlbums")
    plan = fields.Many2one("blooming.membersipplan", ondelete="set null", string="Plan", index=True)