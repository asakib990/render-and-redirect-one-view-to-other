# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class WebView2(http.Controller):
    # Render Form View
    @http.route('/add_new_patient', auth='public', website=True)
    def hospital_patient_new(self, **kw):
        return request.render('web_view2.add_new_patient', {
        })

    # Redirect To  Patient Page
    @http.route('/my_form', auth='public', website=True)
    def hospital_patient_redirect(self, **kw):
        name = kw.get('name')
        email = kw.get('email')
        age = kw.get('age')
        request.env['webview.patient'].create({
            'name': name,
            'email': email,
            'age': age,
        })
        redirect = '/patient_info'
        return request.redirect(redirect)

    # Render Patient Page
    @http.route('/patient_info', auth='public', website=True)
    def hospital_patient(self, **kw):
        # patient = request.env['webview.patient'].search([])
        patient = request.env['webview.patient'].search([])
        return request.render('web_view2.patient_page', {
            'patient': patient,
        })

