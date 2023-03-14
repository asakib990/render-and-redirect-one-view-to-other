# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class WebView(http.Controller):
    @http.route('/my_module', auth='user', website=True, csrf=False)
    def index(self):
        data = request.env['website.data'].search([])
        return request.render('web_view.index', {'data': data})

    @http.route('/my_module/create_data', auth='user', website=True, csrf=False)
    def create_data(self, **post):
        name = post.get('name')
        description = post.get('description')
        date = post.get('date')
        request.env['website.data'].create(
            {'name': name,
             'description': description,
             'date': date})
        return request.redirect('/my_module')


