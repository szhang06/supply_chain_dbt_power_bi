{{
  config(
    materialized='table',
    unique_key='shipment_id'
  )
}}

WITH stg_data AS (
    SELECT
        *,
        ROW_NUMBER() OVER (ORDER BY timestamp) AS shipment_id
    FROM {{ ref('stg_smart_logistics') }}
)

SELECT
    shipment_id,
    asset_id,
    timestamp,
    DATE(timestamp) as date,
    shipment_status,
    is_delayed,
    delay_reason,
    waiting_time_minutes,
    traffic_status,
    temperature,
    humidity,
    CASE WHEN humidity <= 50 THEN 'low'
        WHEN humidity <= 70 THEN 'medium'
        ELSE 'high'
    END AS humidity_level,
    longitude,
    latitude,
    inventory_level,
    user_transaction_amount,
    user_purchase_frequency,
    asset_utilization_percentage,
    demand_forecast
FROM stg_data