SELECT
    state,
    brand,
    SUM(app_opens) AS total_app_opens,
    SUM(registered_users) AS total_registrations
FROM aggregated_user
GROUP BY state, brand
ORDER BY total_app_opens DESC;
