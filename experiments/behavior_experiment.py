import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.behavior_agent import BehavioralAgent
from agents.fraud_agent import FraudDetectionAgent

from utils.preprocessing import load_data, preprocess_data


df = load_data("dataset/creditcard.csv")

X, y = preprocess_data(df)


fraud_agent = FraudDetectionAgent()

fraud_agent.train(X)


behavior_agent = BehavioralAgent()

behavior_agent.build_profile("user1", [50,60,55,65,70])


fraud_only = 0
fraud_behavior = 0


for i in range(100):

    transaction = X.iloc[i].values

    status, score = fraud_agent.predict(transaction)

    if status == "fraud":

        fraud_only += 1


    deviation = behavior_agent.detect_deviation("user1", transaction[-1])

    if status == "fraud" or deviation > 2:

        fraud_behavior += 1


print("Fraud detected (ML only):", fraud_only)

print("Fraud detected (ML + behavior):", fraud_behavior)