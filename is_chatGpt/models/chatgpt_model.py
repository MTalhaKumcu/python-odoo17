# chatgpt_modul.py

from odoo import models, fields, api
import requests

class ChatGPTModel(models.Model):
    _name = 'chatgpt.model'
    _description = 'ChatGPT Model'

    user_input = fields.Char(string="User Input")
    output = fields.Text(string='Output', readonly=True)

    @api.model
    def send_request_to_openai(self, input_text):
        # Burada OpenAI API'sine istek göndermek için gerekli kodları yazmalısınız
        # API anahtarınızı, API'ye istek göndermek için kullanacağınız endpoint'i ve diğer gerekli bilgileri burada tanımlayabilirsiniz.
        # İstek gönderme işlemi için Python'un requests kütüphanesini kullanabilirsiniz
        # Örnek olarak:
        openai_endpoint = 'https://api.openai.com/v1/completions'
        headers = {
            'Authorization': 'Bearer OPENAI KEY',
            'Content-Type': 'application/json'
        }
        data = {
            'model': 'text-davinci-003',  # Gerekli modeli seçiniz
            'prompt': input_text,
            'max_tokens': 50  # İsteğe bağlı, yanıtın maksimum uzunluğunu belirtir
        }
        response = requests.post(openai_endpoint, headers=headers, json=data)
        return response.json().get('choices')[0].get('text')

    def get_output(self):
        for record in self:
            if record.user_input:
                output_text = self.send_request_to_openai(record.user_input)
                record.output = output_text

    def clear_fields(self):
        self.user_input = ''
        self.output = ''

    def button_send_input(self):
        self.get_output()

    def button_clear(self):
        self.clear_fields()
