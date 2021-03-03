from flask import Flask, render_template, request
import joblib
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# halaman home
@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/database', methods=['POST', 'GET'])
# def dataset():
#     pass

@app.route('/visualize', methods=['POST', 'GET'])
def visual():
    return render_template('plot.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method=='POST':
        input = request.form

        df_to_predict = pd.DataFrame({
            'city_development_index': [input['city_development_index']],
            'gender': [input['gender']],
            'relevent_experience': [input['relevent_experience']],
            'enrolled_university': [input['enrolled_university']],
            'education_level': [input['education_level']],
            'major_discipline': [input['major_discipline']],
            'experience': [input['experience']],
            'last_new_job': [input['last_new_job']],
            'training_hours': [input['training_hours']]
        })
        prediksi = model.predict(df_to_predict)

        if prediksi == 0:
            hasil = 'Not Looking for a job change'
        if prediksi == 1:
            hasil = 'Looking for a job change'
        return render_template('result.html', data=input, pred=hasil)

#  Input and Delete
@app.route('/data', methods=['POST', 'GET'])
def data():
    x = pd.read_csv('hrd_for_modelling.csv').drop(['Unnamed: 0'], axis=1)[:100]
    return render_template("data.html", name='HRD', data=x)


if __name__ == '__main__':
    
    filename = 'LogisticRegression.sav'
    model = pickle.load(open(filename,'rb'))

    app.run(debug=True)