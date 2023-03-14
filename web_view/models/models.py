from odoo import models, fields


class MyModuleData(models.Model):
    _name = 'website.data'

    name = fields.Char()
    description = fields.Text()
    date = fields.Date()
