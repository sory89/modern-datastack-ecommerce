{{ config(materialized='table') }}

with cleaned as (
    select
        transaction_id,
        to_timestamp(order_date / 1000)::date as order_date,
        customer_id,
        customer_name,
        case
            when country in ('US', 'UK', 'IN', 'DE', 'FR', 'CA', 'AU') then country
            else 'Unknown'
        end as country,
        product_id,
        product_category,
        case
            when quantity > 0 then quantity
            else 1
        end as quantity,
        case
            when price > 0 then price
            else 0
        end as price,
        order_status
    from {{ ref('br_ecommerce_sales') }}
    where customer_id is not null
        and to_timestamp(order_date / 1000)::date <= current_date
),
deduplicated as (
    select *,
        row_number() over (partition by transaction_id order by order_date desc) as rn
    from cleaned
)
select *
from deduplicated
where rn = 1