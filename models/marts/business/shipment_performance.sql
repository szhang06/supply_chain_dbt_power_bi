{{
  config(
    materialized='table'
  )
}}

WITH shipments AS (
    SELECT
        s.*,
        d.year,
        d.month,
        d.day_of_week
    FROM {{ ref('fact_shipments') }} s
    LEFT JOIN {{ ref('dim_time') }} d ON s.date = d.date
)

SELECT
    asset_id,
    year,
    month,
    day_of_week,
    COUNT(*) AS total_shipments,
    SUM(CASE WHEN is_delayed = 1 THEN 1 ELSE 0 END) AS delayed_shipments,
    AVG(waiting_time_minutes) AS avg_waiting_time,
    AVG(temperature) AS avg_temperature,
    AVG(humidity) AS avg_humidity,
    delay_reason,
    traffic_status,
    SUM(demand_forecast) AS demand_forecast,
    SUM(inventory_level) AS inventory_level
FROM shipments
GROUP BY asset_id, year, month, day_of_week, delay_reason, traffic_status