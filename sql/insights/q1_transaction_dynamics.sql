SELECT
    state,
    year,
    payment_category AS name,
    SUM(count) AS transaction_count,
    SUM(amount) AS total_amount
FROM aggregated_transaction
GROUP BY state, year, payment_category
ORDER BY year, total_amount DESC;

