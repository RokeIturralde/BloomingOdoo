from odoo import api
from odoo import fields
from odoo import models

class Client(models.Model):
    _name = 'blooming.client'
    _inherit = 'res.users'

    sharedAlbums = fields.Many2many("blooming.album",
                                    string="SharedAlbums")
    creators = fields.One2many("blooming.album", "album_id",
                               string="creator")
    plan = fields.Many2one("blooming.membershipplan", ondelete="set null", string="Plan", index=True)
    
    challenges = fields.One2many("blooming.challenge","challenge_id", string = "challenges")