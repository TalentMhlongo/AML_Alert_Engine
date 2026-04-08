# AML Alert Engine

An anti-money laundering (AML) monitoring project built with **SQL**, **Python**, and **Power BI** to identify potentially suspicious deposit activity.

## Business Problem
Financial institutions and betting operators need to monitor customer deposits for unusual patterns that may indicate money laundering, structuring, or other suspicious financial activity.

This project demonstrates how to:
- store transaction and customer data in a relational database,
- query suspicious activity with SQL,
- apply alert logic and risk scoring in Python,
- present AML insights in Power BI.

## Tools Used
- SQL
- Python
- Pandas
- SQLAlchemy
- IBM Db2
- Power BI

## Project Structure
```text
AML_Alert_Engine/
│
├── README.md
├── requirements.txt
│
├── SQL/
│   ├── 01_create_tables.sql
│   ├── 02_insert_mock_data.sql
│   └── 03_monitoring_queries.sql
│
├── python/
│   ├── config.py
│   ├── load_data.py
│   ├── detect_alerts.py
│   ├── export_results.py
│   └── main.py
│
├── data/
│   └── processed/
│       ├── flagged_transactions.csv
│       └── customer_risk_summary.csv
│
└── dashboard/
    └── screenshots/
