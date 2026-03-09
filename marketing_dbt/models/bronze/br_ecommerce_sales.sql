{{ config(materialized='view') }}

SELECT *
FROM {{ source('raw', 'ecommerce_sales') }}