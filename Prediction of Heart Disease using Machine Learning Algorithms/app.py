# Importing essential libraries
from flask import Flask, render_template, request, redirect, url_for, flash
import pickle
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from PIL import Image
import tensorflow as tf

# Load ML model
def ValuePredictor(to_predict_list, size):
    loaded_model = joblib.load('Models/heart-model.pkl')
    to_predict = np.array(to_predict_list).reshape(1, size)
    result = loaded_model.predict(to_predict)
    return result[0]

app = Flask(__name__)
app.secret_key = 'O.\x89\xcc\xa0>\x96\xf7\x871\xa2\xe6\x9a\xe4\x14\x91\x0e\xe5)\xd9'




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/heart')
def heart():
    return render_template('heart.html')


@app.route('/predict_heart', methods=['POST','GET'])
def predict_heart():

    if request.method == 'POST':
        result=request.form
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result1 = ValuePredictor(to_predict_list, 14)
          
        if(int(result1) == 1):
            prediction = 1
        else:
            prediction = 0

        return render_template('h_result.html', prediction=prediction, result=result)


       
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
