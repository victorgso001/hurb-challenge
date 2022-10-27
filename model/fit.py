import pandas as pd
import numpy as np

from flask import Response
from catboost import CatBoostClassifier
from model.preprocess import preprocess
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def fit():
    X_train, X_test, y_train, y_test = preprocess(training=True)
    cat = CatBoostClassifier(iterations=100)
    cat.fit(X_train, y_train)

    y_pred_cat = cat.predict(X_test)

    acc_cat = accuracy_score(y_test, y_pred_cat)
    conf = confusion_matrix(y_test, y_pred_cat)
    clf_report = classification_report(y_test, y_pred_cat)

    cat.save_model('/app/model/data/model')

    return Response("Modelo treinado com sucesso!", status=200)
