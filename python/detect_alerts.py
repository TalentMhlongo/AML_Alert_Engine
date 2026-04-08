from config import (
    THRESHOLD,
    NEAR_THRESHOLD_MIN,
    NEAR_THRESHOLD_MAX,
    STRUCTURING_COUNT,
    HIGH_FREQUENCY_COUNT,
)

def prepare_data(customers, deposits):
    df = deposits.merge(customers, on="customer_id", how="left")
    df["deposit_date"] = df["deposit_date"].astype("datetime64[ns]")
    return df

def apply_rules(df):
    df["flag_high_value"] = (df["amount"] > THRESHOLD).astype(int)

    df["flag_near_threshold"] = df["amount"].between(
        NEAR_THRESHOLD_MIN, NEAR_THRESHOLD_MAX
    ).astype(int)

    near_counts = (
        df.groupby("customer_id")["flag_near_threshold"]
        .sum()
        .reset_index(name="near_threshold_count")
    )
    df = df.merge(near_counts, on="customer_id", how="left")
    df["flag_structuring"] = (df["near_threshold_count"] >= STRUCTURING_COUNT).astype(int)

    txn_counts = (
        df.groupby("customer_id")["deposit_id"]
        .count()
        .reset_index(name="deposit_count")
    )
    df = df.merge(txn_counts, on="customer_id", how="left")
    df["flag_high_frequency"] = (df["deposit_count"] >= HIGH_FREQUENCY_COUNT).astype(int)

    df["flag_high_risk_customer"] = df["risk_rating"].isin(["High", "Medium"]).astype(int)

    df["risk_score"] = (
        df["flag_high_value"] * 3
        + df["flag_structuring"] * 3
        + df["flag_high_frequency"] * 2
        + df["flag_high_risk_customer"] * 2
    )

    df["suspicious_flag"] = (df["risk_score"] >= 5).astype(int)
    return df

def build_customer_summary(df):
    summary = (
        df.groupby(["customer_id", "first_name", "last_name", "risk_rating"], as_index=False)
        .agg(
            total_deposits=("deposit_id", "count"),
            total_amount=("amount", "sum"),
            suspicious_deposits=("suspicious_flag", "sum"),
            max_risk_score=("risk_score", "max"),
        )
    )
    summary["customer_flagged"] = (summary["suspicious_deposits"] > 0).astype(int)
    return summary
