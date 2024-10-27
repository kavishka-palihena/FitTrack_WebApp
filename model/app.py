import pickle
from flask import Flask, render_template, request
import numpy as np
import os

app = Flask(__name__)
def prediction(lst):
    filename = 'model/best_catboost.pkl'
    with open(filename,'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    pred = 0
    if request.method == 'POST':
         # request all the input fields
        gender = object(request.form['gender'])
        age = int(request.form['age'])
        fcvc = float(request.form['fcvc'])
        ch20 = float(request.form['ch20'])
        caec = object(request.form['caec'])
        scc= object(request.form['scc'])
        smoke = object(request.form['smoke'])
        faf = float(request.form['faf'])
        tue = float(request.form['tue'])
        mtrans = object(request.form['mtrans'])


        feature_list = []

        feature_list.append(age)
        feature_list.append(fcvc)
        feature_list.append(ch20 )
        feature_list.append(faf)
        feature_list.append(tue)

        smoke_list = ['yes','no']
        mtrans_list = ['public','walking','automobile', 'motorbike','bike']
        scc_list = ['yes','no']
        gender_list = ['Male', 'Female']
        caec_list = ['sometimes', 'frequent', 'always', 'no']

        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        traverse_list(gender_list, gender)
        traverse_list(caec_list, caec)
        traverse_list(scc_list, scc)
        traverse_list(smoke_list, smoke)
        traverse_list(mtrans_list, mtrans)
        
        pred = prediction(feature_list)

    return render_template("index.html", pred = pred)


if __name__ == '__main__':
    app.run(debug=True)

