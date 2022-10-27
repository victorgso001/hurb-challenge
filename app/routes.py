from flask import Flask, Response, request
from controllers.fit import fit
from controllers.predict import predict
from app import app


@app.route('/')
def index():
    return Response("Hurb Technical Challenge API", status=200)

@app.route('/model/fit')
def fit_model():
    return fit()

@app.route('/model/predict')
def predict_model():
    return predict(request)