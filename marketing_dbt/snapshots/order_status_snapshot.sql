{% snapshot order_status_snapshot %}
{{
    config(
      target_schema='snapshots',
      unique_key='transaction_id',
      strategy='check',
      check_cols=['order_status']
    )
}}
select
    transaction_id,
    customer_id,
    product_id,
    order_date,
    order_status
from {{ ref('sl_ecommerce_sales') }}
{% endsnapshot %}