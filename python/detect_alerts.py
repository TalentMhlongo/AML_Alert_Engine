import pandas as pd
from config import THRESHOLD


def single_large_deposits(df):
    df = df.copy()
    df.columns = df.columns.str.lower()

    alerts = df[
        (df["amount"] >= THRESHOLD)
    ].copy()

    alerts["alert_type"] = "Single Large Deposit"
    alerts["alert_reason"] = "Deposit exceeds R50,000"
    alerts["amount_flagged"] = alerts["amount"]

    return alerts


def monthly_aggregation(df):
    df = df.copy()
    df.columns = df.columns.str.lower()

    df["deposit_date"] = pd.to_datetime(df["deposit_date"])
    df["year_month"] = df["deposit_date"].dt.to_period("M")

    monthly = (
        df.groupby(["customer_id", "year_month"])["amount"]
        .sum()
        .reset_index()
    )

    alerts = monthly[monthly["amount"] >= THRESHOLD].copy()

    alerts["alert_type"] = "Monthly Aggregate"
    alerts["alert_reason"] = "Monthly deposits exceed threshold"
    alerts["amount_flagged"] = alerts["amount"]

    return alerts

def high_frequency(df, threshold_count=5):
    df = df.copy()
    df.columns = df.columns.str.lower()

    df["deposit_date"] = pd.to_datetime(df["deposit_date"])
    df["transaction_day"] = df["deposit_date"].dt.date

    frequency = (
        df.groupby(["customer_id", "transaction_day"])
        .size()
        .reset_index(name="transaction_count")
    )

    alerts = frequency[frequency["transaction_count"] >= threshold_count].copy()

    alerts["alert_type"] = "High Frequency Transactions"
    alerts["alert_reason"] = f"{threshold_count} or more transactions in one day"

    return alerts
