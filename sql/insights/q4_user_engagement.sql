SELECT
    state,
    SUM(app_opens) AS total_app_opens,
    SUM(registered_users) AS total_users
FROM map_user
GROUP BY state
ORDER BY total_app_opens DESC;
