from catboost import CatBoostClassifier
from flask import Response, jsonify
import pandas as pd
import os

from utils.preprocess import preprocess


def predict(request):
    data = request.get_json()
    data = pd.DataFrame([data])

    try:
        data_to_predict = preprocess(df=data)
    except:
        return Response(
            "reservation_status_date not valid. Only valid with year between 2014 to 2017.",
            status=400
            )

    if not (os.path.isfile('/app/model/catboost')):
        return Response('There is no model to perform prediction on.', status=400)

    model = CatBoostClassifier()
    model.load_model('/app/model/catboost')

    prediction = model.predict(data_to_predict)

    print("pred_class", flush=True)
    print(type(prediction[0].item()), flush=True)

    response={
            "pred_class": prediction[0].item(),
        }

    return response
