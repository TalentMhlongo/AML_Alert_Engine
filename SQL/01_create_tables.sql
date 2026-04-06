DROP TABLE IF EXISTS HWB_customers;
DROP TABLE IF EXISTS HWB_deposits;
DROP TABLE IF EXISTS HWB_aml_alerts;

CREATE TABLE HWB_customers (
    customer_id INT NOT NULL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    country VARCHAR(50),
    account_status VARCHAR(20),
    risk_rating VARCHAR(20),
    registration_date DATE
);

CREATE TABLE HWB_deposits (
    deposit_id INT NOT NULL PRIMARY KEY,
    customer_id INT,
    deposit_date TIMESTAMP,
    amount DECIMAL(12,2),
    payment_method VARCHAR(30),
    source_channel VARCHAR(30),
    status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES HWB_customers(customer_id)
);

CREATE TABLE HWB_aml_alerts (
    alert_id INT GENERATED ALWAYS AS IDENTITY,
    deposit_id INT,
    customer_id INT,
    alert_date TIMESTAMP,
    alert_type VARCHAR(100),
    threshold_amount DECIMAL(12,2),
    deposit_amount DECIMAL(12,2),
    alert_status VARCHAR(30),
    investigator VARCHAR(100)
);
