# -*- coding: utf-8 -*-

from odoo import http

class GptController(http.Controller):
    @http.route(['/chatgpt_form'], type='http',auto="public",
                                    csrf=False , website=True)
    def question_submit(self):
        return http.request.render('is_chatGpt_new.connector')
    