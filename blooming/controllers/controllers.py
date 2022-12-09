# -*- coding: utf-8 -*-
from odoo import http

# class Blooming(http.Controller):
#     @http.route('/blooming/blooming/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/blooming/blooming/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('blooming.listing', {
#             'root': '/blooming/blooming',
#             'objects': http.request.env['blooming.blooming'].search([]),
#         })

#     @http.route('/blooming/blooming/objects/<model("blooming.blooming"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('blooming.object', {
#             'object': obj
#         })