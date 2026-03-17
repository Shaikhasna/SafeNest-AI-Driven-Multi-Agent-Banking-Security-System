import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np

from models.autoencoder import build_autoencoder
from utils.preprocessing import load_data, preprocess_data


df = load_data("dataset/creditcard.csv")

X, y = preprocess_data(df)


X_train = X[y == 0]


model = build_autoencoder(X.shape[1])


model.fit(
    X_train,
    X_train,
    epochs=5,
    batch_size=256
)


reconstructions = model.predict(X)

mse = np.mean(np.power(X - reconstructions, 2), axis=1)

print("Autoencoder anomaly scores generated")