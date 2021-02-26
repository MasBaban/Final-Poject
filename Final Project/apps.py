rom flask import Flask, render_template, request, session, redirect
import numpy as np
import pandas as pd
import seaborn as sb
import plotly
import plotly.graph_objs as go
import mysql.connector
# Data dari flask di kirim ke browser dalam bentuk json
import json
import joblib
import pickle

# Sumber Data
dst = pd.read_csv('dst1.csv').set_index('Unnamed: 0')



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Render Picture
@app.route('/static/<path:x>')
def gal(x):
    return send_from_directory("static", x)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    return render_template('predict.html')
'''
'gender', 'Relevent Experience', 'Enrolled University', 'Education Level',
 'Major Discipline', 'Experience', 'Company Size', Company Type, Last New Job, 'Training Hours'
'''
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method=='POST':
        input = request.form