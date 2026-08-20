-- Revenue by minute
SELECT DATE_TRUNC('minute', event_time) AS minute,
       COUNT(*) AS transactions,
       SUM(amount) AS revenue
FROM transactions
GROUP BY 1
ORDER BY 1;

-- High-value events
SELECT event_id, customer_id, amount, event_time
FROM transactions
WHERE amount >= 250
ORDER BY event_time DESC;
