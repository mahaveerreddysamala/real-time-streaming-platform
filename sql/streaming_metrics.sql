CREATE TABLE IF NOT EXISTS transaction_minute_metrics (
    window_start TIMESTAMP NOT NULL,
    window_end TIMESTAMP NOT NULL,
    transaction_count INTEGER NOT NULL,
    revenue NUMERIC(14,2) NOT NULL,
    PRIMARY KEY (window_start, window_end)
);

-- Dashboard query: revenue by five-minute window
SELECT window_start, window_end, transaction_count, revenue
FROM transaction_minute_metrics
ORDER BY window_start DESC;
