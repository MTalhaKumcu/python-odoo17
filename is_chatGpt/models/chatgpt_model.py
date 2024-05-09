# chatgpt_modul.py

import json
from odoo import models, fields, api
import requests

class ChatGPTModel(models.Model):
    _name = 'chatgpt.model'
    _description = 'ChatGPT Model'

    user_input = fields.Char(string="User Input")
    output = fields.Text(string='Output', readonly=True)

    @api.model
    def send_request_to_openai(self, input_text):
        # Here you should write the code to send a request to the OpenAI API
        # Here you can define your API key, the endpoint you will use to send requests to the API, and other necessary information.
        # You can use Python's requests library for sending requests
        3
        openai_endpoint = 'https://api.openai.com/v1/chat/completions'
        headers = {
            'Authorization': 'Bearer YOUR API',
            'Content-Type': 'application/json'
        }
        data = {
            'model': 'gpt-3.5-turbo',  # Select the required model
            'messages': [{'role': 'user', 'content': input_text}],
            'max_tokens': 500  # Optional, specifies the maximum length of the response
        }
            
        try:
            
            response = requests.post(openai_endpoint, headers=headers, json=data)
            response.raise_for_status()  # Raise error in case of error
            response_json = response.json()  # Get JSON content
            output_text = response_json['choices'][0]['message']['content'] # Convert Json to Text

            return output_text
           
        except requests.exceptions.RequestException as e:
            print("İstek hatas:", e)
            return str(e)
        
    def get_output(self):
        for record in self:
            if record.user_input:
                output_text = self.send_request_to_openai(record.user_input)
                                
                if output_text is not None:
                    record.output = output_text
                else:
                    record.output = "something wrong"
    
    def clear_fields(self):
        self.user_input = ''
        self.output = ''

    def button_send_input(self):
        self.get_output()

    def button_clear(self):
        self.clear_fields()
