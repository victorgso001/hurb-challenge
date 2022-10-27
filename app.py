from flask import Flask, Response, request


from controllers.fit import fit
from controllers.predict import predict

app = Flask(__name__)

@app.route('/')
def test():
    return Response("Hurb Technical Challenge API", status=200)

@app.route('/model/fit')
def fit_model():
    return fit()

@app.route('/model/predict')
def predict_model():
    return predict(request)

if __name__ == '__main__':
    app.run(debug=True, port=6000, host='0.0.0.0')