from odoo import api
from odoo import fields
from odoo import models

class MembershipPlan(models.Model):
    _name = 'blooming.membershipplan'
    name = fields.Char()
    albumLimit = fields.Integer()
    description = fields.Char()
    duration = fields.Integer()
    price = fields.Float()
    shareable = fields.Boolean()
    user_ids = fields.One2many("blooming.client", "id", string="User ids")