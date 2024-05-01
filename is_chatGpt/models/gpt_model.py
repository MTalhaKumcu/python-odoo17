# -*- coding: utf-8 -*-

from odoo import api, fields, models
import requests


class GPTModel(models.Model):
    _name = "gpt.model"
    _description = "ChatGPT Model"

    name = fields.Char(string="ChatGPT Model", required=True)
    description = fields.Text(string="Description")

    @api.model
    def generate_text(self, prompt):
        url = "https://api.openai.com/v1/completions"
        headers = {
            "Content-Type": "application/json",
            # "Authorization": "Bearer YOUR OPEN AI API",
            # write here your AI API and delete "hash"
        }
        data = {"model": "text-davinci-003", "prompt": prompt, "max_tokens": 500}
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["text"]
        else:
            return "Error: Failed to generate text. Status code: {}".format(
                response.status_code
            )