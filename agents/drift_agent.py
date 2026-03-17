import numpy as np

class DriftAgent:

    def __init__(self):
        self.history = {}

    def update_history(self, user_id, amount):

        if user_id not in self.history:
            self.history[user_id] = []

        self.history[user_id].append(amount)


    def detect_drift(self, user_id):

        data = self.history.get(user_id, [])

        if len(data) < 10:
            return False

        mean = np.mean(data[:-1])
        latest = data[-1]

        if abs(latest - mean) > 3 * np.std(data):

            return True

        return False