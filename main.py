import random

from utils.preprocessing import load_data, preprocess_data

from agents.fraud_agent import FraudDetectionAgent
from agents.behavior_agent import BehavioralAgent
from agents.coordinator_agent import CoordinatorAgent
from agents.compliance_agent import ComplianceAgent


df = load_data("dataset/creditcard.csv")

X, y = preprocess_data(df)


fraud_agent = FraudDetectionAgent()

fraud_agent.train(X)


behavior_agent = BehavioralAgent()

behavior_agent.build_profile(
    "user1",
    [50, 60, 55, 65, 70]
)


coordinator = CoordinatorAgent(
    fraud_agent,
    behavior_agent
)


compliance = ComplianceAgent()


for i in range(10):

    transaction = X.iloc[random.randint(0, len(X)-1)].values

    decision, risk = coordinator.evaluate_transaction(
    "user1",
    transaction
)

    compliance.log_event("user1", decision)

    print("Transaction", i, "Decision:", decision, "Risk Score:", risk)