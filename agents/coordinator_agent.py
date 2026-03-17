class CoordinatorAgent:

    def __init__(self, fraud_agent, behavior_agent):

        self.fraud_agent = fraud_agent
        self.behavior_agent = behavior_agent


    def evaluate_transaction(self, user_id, transaction):

        fraud_status, anomaly_score = self.fraud_agent.predict(transaction)

        deviation = self.behavior_agent.detect_deviation(
            user_id,
            transaction[-1]
        )

        # normalize anomaly score
        anomaly_risk = abs(anomaly_score) * 50

        behavior_risk = deviation * 10

        risk_score = anomaly_risk + behavior_risk


        if risk_score > 70:

            decision = "BLOCK"

        elif risk_score > 40:

            decision = "ALERT"

        else:

            decision = "ALLOW"


        return decision, risk_score