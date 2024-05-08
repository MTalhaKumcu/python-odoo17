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
        # Burada OpenAI API'sine istek göndermek için gerekli kodları yazmalısınız
        # API anahtarınızı, API'ye istek göndermek için kullanacağınız endpoint'i ve diğer gerekli bilgileri burada tanımlayabilirsiniz.
        # İstek gönderme işlemi için Python'un requests kütüphanesini kullanabilirsiniz
        # Örnek olarak:
        openai_endpoint = 'https://api.openai.com/v1/completions'
        headers = {
            'Authorization': 'Bearer YOUR OPEN AI API',
            'Content-Type': 'application/json'
        }
        data = {
            'model': 'gpt-3.5-turbo',  # Gerekli modeli seçiniz
            'prompt': input_text,
            'max_tokens': 500  # İsteğe bağlı, yanıtın maksimum uzunluğunu belirtir
        }
            
        try:
            
            response = requests.post(openai_endpoint, headers=headers, json=data)
            response.raise_for_status()  # Hata durumunda hata yükselt
            response_json = response.json()  # JSON içeriğini al
            #return response_json
            choices = response_json.get('choices')

            if choices and isinstance(choices, list) and choices[0].get('text'):
                return choices[0].get('text')  # Yanıtı döndür
            else:
                print("Beklenmeyen yant format:", response.text)
                return None
        except requests.exceptions.RequestException as e:
            print("İstek hatas:", e)
            return str(e)
        
    def get_output(self):
        for record in self:
            if record.user_input:
                output_text = self.send_request_to_openai(record.user_input)
                #record.output = output_text
                
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
