# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class ProductProduct(models.Model):
    _inherit = "product.product"
    _description = "Products"

    is_admission_product = fields.Boolean(string="Admission Product", default=False)

