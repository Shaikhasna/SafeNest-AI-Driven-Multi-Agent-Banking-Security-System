import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import shap

from sklearn.ensemble import IsolationForest

from utils.preprocessing import load_data, preprocess_data


df = load_data("dataset/creditcard.csv")

X, y = preprocess_data(df)


model = IsolationForest(contamination=0.002)

model.fit(X)


explainer = shap.Explainer(model)

shap_values = explainer(X[:1000])


shap.plots.bar(shap_values)