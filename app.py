import pandas as pd 
import numpy as np 
from flask import Flask , render_template, redirect , url_for, request
import os
import pickle
pkl_file_path = os.path.join(os.path.dirname(__file__), 'diabetes.pkl')
model = pickle.load(open(pkl_file_path, 'rb'))


app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
                                
def check():
    
    preg= int(request.form.get('preg'))
    glucose= int(request.form.get('glucose'))
    bp= int(request.form.get('bp'))
    skin_thikness= int(request.form.get('skin_thikness'))
    insulin= int(request.form.get('insulin'))
    bmi= float(request.form.get('bmi'))
    dia_func= int(request.form.get('diabetes_func'))
    age_var= int(request.form.get('age'))
    
    result = model.predict([[preg,glucose,bp,skin_thikness,insulin,bmi,dia_func,age_var]])
    output = int(result[0])
    
    
    if output == 1:
        return "<h1>Patient is Diabetic positive</h1>"
    else :
        return "<h1>No symptoms of Diabetes</h1>"

                                

if __name__=="__main__":
    app.run(debug=True)