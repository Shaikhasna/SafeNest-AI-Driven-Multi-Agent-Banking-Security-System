from sklearn.ensemble import IsolationForest

class FraudDetectionAgent:

    def __init__(self):

        self.model = IsolationForest(
            n_estimators=100,
            contamination=0.002,
            random_state=42
        )

    def train(self, X):

        self.model.fit(X)

    def predict(self, transaction):

        score = self.model.decision_function([transaction])

        pred = self.model.predict([transaction])

        if pred[0] == -1:

            return "fraud", score[0]

        else:

            return "normal", score[0]