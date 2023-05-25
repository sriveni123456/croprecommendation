import json
import requests


url = ''

input_data_for_model = {
    
    'N' : 5,
    'P' : 166,
    'K' : 72,
    'tempurature' : 19,
    'humidity' : 175,
    'ph' : 25.8,
    'rainfall' : 0.587,
    
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)
