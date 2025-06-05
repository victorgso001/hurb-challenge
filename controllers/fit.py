import pandas as pd
import numpy as np

import mlflow
from flask import Response
from catboost import CatBoostClassifier
from utils.preprocess import preprocess

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)


def fit():
    """Fit and save model, generating metrics for MLFlow model log."""
    params = {
        "iterations": 100,
    }

    X_train, X_test, y_train, y_test = preprocess(training=True)


    cat = CatBoostClassifier(iterations=100)

    cat.fit(X_train, y_train)

    y_pred = cat.predict(X_test)

    acc_cat = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_pred)

    experiment_name = "MLOps Challenge"

    mlflow.set_experiment(experiment_name=experiment_name)

    with mlflow.start_run() as run:
        mlflow.log_params(params)
        mlflow.catboost.log_model(cat, artifact_path="model")
        mlflow.log_metric("accuracy", acc_cat)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)
        mlflow.log_metric("area_under_roc_curve", auc)

    cat.save_model('/app/model/catboost')

    return Response("Model trained successfully!", status=200)
