# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WebView2(models.Model):
    _name = 'webview.patient'
    _description = 'web_view2.web_view2'

    name = fields.Char()
    email = fields.Char()
    age = fields.Integer()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
