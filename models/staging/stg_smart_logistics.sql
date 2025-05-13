 {{
  config(
    materialized='view'
  )
}}

WITH source AS (
    SELECT * FROM {{ source('staging', 'slchain_data') }} -- source name, table name
),

renamed AS (
    SELECT
        -- Timestamps
        Timestamp AS timestamp,

        -- Asset information
        Asset_ID AS asset_id,

        -- Location data
        Latitude AS latitude,
        Longitude AS longitude,
        
        -- Inventory and shipment status
        Inventory_Level AS inventory_level,
        Shipment_Status AS shipment_status,
        
        -- Environmental conditions
        Temperature AS temperature,
        Humidity AS humidity,
    
        -- Traffic and waiting
        Traffic_Status AS traffic_status,
        Waiting_Time AS waiting_time_minutes,
        
        -- User activity
        User_Transaction_Amount AS user_transaction_amount,
        User_Purchase_Frequency AS user_purchase_frequency,
        
        -- Delay information
        Logistics_Delay_Reason AS delay_reason,
        Logistics_Delay AS is_delayed,
        
        -- Utilization metrics
        Asset_Utilization AS asset_utilization_percentage,
        Demand_Forecast AS demand_forecast
        
    FROM source
)

SELECT * FROM renamed