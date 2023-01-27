# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MembershipPlan(models.Model):
    _name = 'blooming.membershipplan'
    name = fields.Char()
    albumLimit = fields.Integer()
    description = fields.Char()
    duration = fields.Integer()
    price = fields.Float()
    shareable = fields.Boolean()
    user_ids = fields.One2many("res.users", "id", string="User ids")
    
    
    
#    @api.constrains('price')
#    def _check_price(self):
#        #for record in self:
#        if self.price < 0:
#            raise ValidationError("The price cannot be lower than 0: %s" % self.age)
#    
    
    
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

