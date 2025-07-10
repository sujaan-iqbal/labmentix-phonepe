SELECT
    state,
    year,
    insurance_type,
    SUM(count) AS insurance_transactions,
    SUM(amount) AS insurance_amount
FROM aggregated_insurance
GROUP BY state, year, insurance_type
ORDER BY year, insurance_amount DESC;
