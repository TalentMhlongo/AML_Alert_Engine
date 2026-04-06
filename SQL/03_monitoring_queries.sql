SELECT
    d.deposit_id,
    d.customer_id,
    c.first_name,
    c.last_name,
    c.risk_rating,
    d.deposit_date,
    d.amount,
    d.payment_method,
    d.source_channel
FROM HWB_deposits d
JOIN HWB_customers c
    ON d.customer_id = c.customer_id
WHERE d.amount > 50000
ORDER BY d.amount DESC;
