SELECT
    state,
    region,
    SUM(count) AS transaction_count,
    SUM(amount) AS transaction_value
FROM top_transaction
GROUP BY state, region
ORDER BY transaction_value DESC
LIMIT 10;
