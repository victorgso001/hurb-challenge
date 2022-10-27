from flask import Flask, Response

from catboost import CatBoostClassifier
from model.fit import fit
import os

app = Flask(__name__)

@app.route('/')
def test():
    return Response("First API test page", status=200)

@app.route('/model/fit')
def fit_model():
    return fit()

@app.route('/model/predict')
def predict_model():
        # if (os.path.isfile('/app/model/data/model')):
        # model = CatBoostClassifier()
        # model.load('/app/model/data/model')
        # TODO: Prediction route

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')