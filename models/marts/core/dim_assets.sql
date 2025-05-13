{{
  config(
    materialized='table',
    unique_key='asset_id'
  )
}}

SELECT
    asset_id,
    COUNT(*) AS total_shipments,
    AVG(inventory_level) AS avg_inventory_level,
    AVG(asset_utilization_percentage) AS avg_utilization,
    AVG(waiting_time_minutes) AS avg_waiting_time
FROM {{ ref('stg_smart_logistics') }}
GROUP BY asset_id