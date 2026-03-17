import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import numpy as np

from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM

from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

from utils.preprocessing import load_data, preprocess_data


df = load_data("dataset/creditcard.csv")

X, y = preprocess_data(df)
# use smaller sample for faster experiment
X = X.sample(10000, random_state=42)
y = y.loc[X.index]


X_train = X[y == 0]

X_test = X
y_test = y


models = {

    "IsolationForest": IsolationForest(contamination=0.002),

    "LOF": LocalOutlierFactor(novelty=True),

    "OneClassSVM": OneClassSVM(nu=0.002)

}


results = []


for name, model in models.items():

    model.fit(X_train)

    preds = model.predict(X_test)

    preds = np.where(preds == -1, 1, 0)

    precision = precision_score(y_test, preds)
    recall = recall_score(y_test, preds)
    f1 = f1_score(y_test, preds)

    results.append([name, precision, recall, f1])


results_df = pd.DataFrame(
    results,
    columns=["Model", "Precision", "Recall", "F1"]
)


print(results_df)


results_df.to_csv("results/model_comparison.csv", index=False)