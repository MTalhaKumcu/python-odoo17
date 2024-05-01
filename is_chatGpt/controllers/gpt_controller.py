# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import requests

class GPTController(http.Controller):

    @http.route('/generate_text', type='http',
                                  auth='user',
                                  csrf=False,
                                  website=True)
    def generate_text(self, **kwargs):
        return http.request.render('is_chatGpt.connector')