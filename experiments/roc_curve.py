import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
import numpy as np

from sklearn.ensemble import IsolationForest
from sklearn.metrics import roc_curve, auc

from utils.preprocessing import load_data, preprocess_data


df = load_data("dataset/creditcard.csv")

X, y = preprocess_data(df)


model = IsolationForest(contamination=0.002)

model.fit(X[y == 0])


scores = model.decision_function(X)

fpr, tpr, _ = roc_curve(y, -scores)

roc_auc = auc(fpr, tpr)


plt.figure()

plt.plot(fpr, tpr, label="ROC curve (area = %0.2f)" % roc_auc)

plt.plot([0, 1], [0, 1], linestyle="--")

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("ROC Curve - Fraud Detection")

plt.legend(loc="lower right")

plt.savefig("plots/roc_curve.png")

plt.show()