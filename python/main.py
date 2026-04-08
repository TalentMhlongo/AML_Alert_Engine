from load_data import load_all_data
from detect_alerts import prepare_data, apply_rules, build_customer_summary
from export_results import export_results

def main():
    customers, deposits = load_all_data()

    df = prepare_data(customers, deposits)
    df = apply_rules(df)

    flagged_transactions = df[df["suspicious_flag"] == 1].copy()
    customer_summary = build_customer_summary(df)

    export_results(flagged_transactions, customer_summary)

    print("AML alert engine completed successfully.")
    print("Flagged transactions:", len(flagged_transactions))
    print("Flagged customers:", customer_summary["customer_flagged"].sum())

if __name__ == "__main__":
    main()
