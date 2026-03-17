import numpy as np

class BehavioralAgent:

    def __init__(self):

        self.user_profiles = {}

    def build_profile(self, user_id, transactions):

        avg_amount = np.mean(transactions)

        self.user_profiles[user_id] = avg_amount


    def detect_deviation(self, user_id, transaction_amount):

        baseline = self.user_profiles.get(user_id, None)

        if baseline is None:

            return 0

        deviation = abs(transaction_amount - baseline)

        return deviation