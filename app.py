# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 23:48:20 2020

@author: Avijit Banduri
"""

import numpy as np
from flask import Flask, request, render_template
from model import recommend_movie

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=["GET", "POST"])
def predict():
    name = request.form['Movie_Name']
    output=recommend_movie(name)
    return render_template('index.html', mov_name=name, prediction=output)

if __name__ == "__main__":
    app.run(debug=True)