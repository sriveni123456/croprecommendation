from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

class model_input(BaseModel):
    N	:int
    P        :        int
    K         :       int
    temperature  :  float
    humidity   :    float
    ph         :    float
    rainfall   :    float
    
  
        
# loading the saved model
model = pickle.load(open('crop.sav', 'rb'))

@app.post('/crop_prediction')
def diabetes_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['N']
    glu = input_dictionary['P']
    bp = input_dictionary['K']
    skin = input_dictionary['temperature']
    insulin = input_dictionary['humidity']
    bmi = input_dictionary['ph']
    dpf = input_dictionary['rainfall']
    
    
    
    input_list = [preg, glu, bp, skin, insulin, bmi, dpf]
    
    prediction = model.predict([input_list])
    
   