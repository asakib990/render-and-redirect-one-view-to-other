# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class SeStudent(models.Model):
    _inherit = "se.student"
    _description = "Students"

    # application_ids = fields.One2many(comodel_name="se.application", inverse_name='student_id',
    #                                   string="Admission Applications")
    emergency_contact_info = fields.Char(string='Emergency Contact')

