import pickle
from flask import Flask, render_template, request
import numpy as np
import os
import pandas as pd

app = Flask(__name__)

filename = 'model/best_model.pkl'
with open(filename,'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['POST', 'GET'])
def index():
    prediction = None
    full_name = None
    if request.method == 'POST': 
    # Extract data from the form
        full_name = request.form.get('name')
        Gender = request.form.get('gender')
        Age = request.form.get('age')
        FCVC = request.form.get('fcvc')
        CH2O = request.form.get('ch2o')
        CAEC = request.form.get('caec')
        SCC = request.form.get('scc')
        SMOKE = request.form.get('smoke')
        FAF = request.form.get('faf')
        TUE = request.form.get('tue')
        MTRANS = request.form.get('mtrans')
    
    

        # You can now feed this data into your model or process it as needed
        # For example, let's print the data to console (you can replace this with your model prediction logic)
        print(f"Name: {full_name}, Gender: {Gender}, Age: {Age}")
        print(f"Vegetable Consumption: {FCVC}, Water Consumption: {CH2O}L/day")
        print(f"Food Between Meals: {CAEC}, Calorie Monitoring: {SCC}")
        print(f"Smoking: {SMOKE}, Physical Activity: {FAF}, Tech Use: {TUE}")
        print(f"Transportation: {MTRANS}")
        input = {'Age' : [Age], 'FCVC': [FCVC], 'CH2O' : [CH2O], 'FAF': [FAF], 'TUE': [TUE], 'SMOKE': [SMOKE], 'MTRANS' : [MTRANS], 'SCC' : [SCC], 'Gender' : [Gender], 'CAEC' : [CAEC]}
        input_df = pd.DataFrame(input)
        prediction = model.predict(input_df)[0]
        #return f"The nutritional level of {full_name} is: {prediction[0]}"
    return render_template("index.html", pred = prediction, name=full_name)

if __name__ == '__main__':
    app.run(debug=True)