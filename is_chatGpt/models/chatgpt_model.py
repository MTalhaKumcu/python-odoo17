# chatgpt_model.py

from odoo import api, fields, models

import openai

class GptModel(models.Model):
    _name = "chatgpt.model"
    _description = "ChatGPT Model"

    name = fields.Char(string="ChatGPT Model", required=True)
    user_input = fields.Text(string="user_input")  # Yeni eklenen alan
    output_message = fields.Text(string="output_message", readonly=True)
    
    # Initialize OpenAI API with your API key
    openai.api_key = "sk-proj-EqtjXP4stqo4E2SsMWCMT3BlbkFJrRnsObvIazbOHAG9XEKr"

    @api.model
    def generate_response(self, prompt):
        # Generate response using OpenAI's completion endpoint
        completion = openai.Completion.create(
            engine="davinci",  # You can choose the language model you prefer
            prompt=prompt,
            max_tokens=250,  # Maximum number of tokens in the generated response
        )
        return completion.choices[0].text.strip()

    @api.multi
    def send_user_input(self):
        self.ensure_one()
        prompt = self.user_input
        response = self.generate_response(prompt)
        self.output_message = response 
