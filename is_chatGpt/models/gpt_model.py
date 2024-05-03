# -*- coding: utf-8 -*-

from odoo import api,fields, models

import openai

class GptModel(models.Model):
    _name = "chatgpt.model"
    _description = "ChatGPT Model"

    name = fields.Char(string='ChatGPT Model', required=True)

    # Initialize OpenAI API with your API key
    openai.api_key = 'API KEY'

    @api.model
    def generate_response(self, prompt):
        # Generate response using OpenAI's completion endpoint
        completion = openai.Completion.create(
            engine="davinci",  # You can choose the language model you prefer
            prompt=prompt,
            max_tokens=150  # Maximum number of tokens in the generated response
        )
        return completion.choices[0].text.strip()
