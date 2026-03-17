from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model


def build_autoencoder(input_dim):

    input_layer = Input(shape=(input_dim,))

    encoded = Dense(16, activation="relu")(input_layer)
    encoded = Dense(8, activation="relu")(encoded)

    decoded = Dense(16, activation="relu")(encoded)
    decoded = Dense(input_dim, activation="sigmoid")(decoded)

    autoencoder = Model(input_layer, decoded)

    autoencoder.compile(
        optimizer="adam",
        loss="mse"
    )

    return autoencoder