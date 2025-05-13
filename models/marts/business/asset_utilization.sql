{{
  config(
    materialized='table'
  )
}}

SELECT
    a.asset_id,
    a.avg_inventory_level,
    a.avg_utilization,
    COUNT(DISTINCT s.date) AS active_days,
    COUNT(*) AS total_shipments,
    SUM(CASE WHEN s.is_delayed = 1 THEN 1 ELSE 0 END) AS delayed_shipments,
    AVG(s.waiting_time_minutes) AS avg_waiting_time
FROM {{ ref('dim_assets') }} a
JOIN {{ ref('fact_shipments') }} s ON a.asset_id = s.asset_id
GROUP BY a.asset_id, a.avg_inventory_level, a.avg_utilization