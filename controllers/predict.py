from catboost import CatBoostClassifier
from flask import Response, jsonify
import pandas as pd
import os

from utils.preprocess import preprocess


def predict(request):
    data = request.get_json()
    data = pd.DataFrame([data])
    data_to_predict = preprocess(df=data)

    if not (os.path.isfile('/app/model/data/catboost')):
        return Response('There is no model to perform prediction.', status=400)

    model = CatBoostClassifier()
    model.load_model('/app/model/data/model')

    prediction = model.predict(data_to_predict)

    print("pred_class", flush=True)
    print(type(prediction[0].item()), flush=True)

    response={
            "pred_class": prediction[0].item(),
        }

    return response
        