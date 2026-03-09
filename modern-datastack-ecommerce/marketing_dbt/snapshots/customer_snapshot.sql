{% snapshot customer_snapshot %}
{{
    config(
      target_schema='snapshots',
      unique_key='customer_id',
      strategy='check',
      check_cols=['customer_name', 'country']
    )
}}
select distinct
    customer_id,
    customer_name,
    country
from {{ ref('sl_ecommerce_sales') }}
{% endsnapshot %}