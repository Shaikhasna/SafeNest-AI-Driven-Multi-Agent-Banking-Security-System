import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

from sklearn.ensemble import IsolationForest

from utils.preprocessing import load_data, preprocess_data


df = load_data("dataset/creditcard.csv")

X, y = preprocess_data(df)


model = IsolationForest(contamination=0.002)

model.fit(X[y == 0])


scores = -model.decision_function(X)


precision, recall, _ = precision_recall_curve(y, scores)


plt.figure()

plt.plot(recall, precision)

plt.xlabel("Recall")

plt.ylabel("Precision")

plt.title("Precision-Recall Curve")

plt.savefig("plots/pr_curve.png")

plt.show()