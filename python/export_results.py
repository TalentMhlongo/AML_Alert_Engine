import os
from config import PROCESSED_DATA_PATH

def export_results(flagged_transactions, customer_summary):
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

    flagged_transactions.to_csv(
        os.path.join(PROCESSED_DATA_PATH, "flagged_transactions.csv"),
        index=False
    )

    customer_summary.to_csv(
        os.path.join(PROCESSED_DATA_PATH, "customer_risk_summary.csv"),
        index=False
    )
