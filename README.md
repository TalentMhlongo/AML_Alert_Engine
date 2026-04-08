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

  ## Data Source Options

This project supports two input methods:

### 1. CSV Files (Default)
The default version reads `customers.csv` and `deposits.csv` from the `data/raw/` folder. This makes the project easy to run locally and easy for review.

### 2. IBM Db2 (Optional)
The project also supports reading customer and deposit data directly from IBM Db2 using environment variables for connection details.


## Project Structure
```text
AML_Alert_Engine/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   └── deposits.csv
│   │
│   └── processed/
│       ├── flagged_transactions.csv
│       └── customer_risk_summary.csv
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
└── dashboard/
    ├── aml_dashboard.pbix
    └── screenshots/

