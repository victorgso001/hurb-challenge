from catboost import CatBoostClassifier
from flask import Response, jsonify
import pandas as pd
import os

from utils.preprocess import preprocess


def predict(request):
    """Predict Cancellation EDA based on JSON with the same columns as documented."""
    data = request.get_json()
    data = pd.DataFrame([data])

    data_to_predict = preprocess(df=data)


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
