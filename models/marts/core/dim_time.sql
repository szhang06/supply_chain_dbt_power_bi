{{
  config(
    materialized='table',
    unique_key='date'
  )
}}

SELECT
    date,
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(MONTH FROM date) AS month,
    EXTRACT(DAY FROM date) AS day,
    EXTRACT(DAYOFWEEK FROM date) AS day_of_week, 
    EXTRACT(QUARTER FROM date) AS quarter,
    EXTRACT(DAYOFYEAR FROM date) AS day_of_year
FROM (
    SELECT DISTINCT DATE(timestamp) AS date 
    FROM {{ ref('stg_smart_logistics') }}
)