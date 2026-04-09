from load_data import load_all_data
from detect_alerts import single_large_deposits, monthly_aggregation, high_frequency
from export_results import export_to_csv


def main():
    print("Loading data from CSV files...")
    customers, deposits = load_all_data()

    print(f"Customers loaded: {len(customers)}")
    print(f"Deposit loaded: {len(deposits)}")

    single_alerts = single_large_deposits(deposits)
    monthly_alerts = monthly_aggregation(deposits)
    freq_alerts = high_frequency(deposits)

    print(f"Single alerts: {len(single_alerts)}")
    print(f"Monthly alerts: {len(monthly_alerts)}")
    print(f"Frequency alerts: {len(freq_alerts)}")

    export_to_csv(single_alerts, "single_large_deposit_alerts.csv")
    export_to_csv(monthly_alerts, "monthly_aggregate_alerts.csv")
    export_to_csv(freq_alerts, "high_frequency_alerts.csv")

    print("AML process complete.")


if __name__ == "__main__":
    main()
