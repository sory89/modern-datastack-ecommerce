{% snapshot product_snapshot %}
{{
    config(
      target_schema='snapshots',
      unique_key='product_id',
      strategy='check',
      check_cols=['product_category']
    )
}}
select distinct
    product_id,
    product_category
from {{ ref('sl_ecommerce_sales') }}
{% endsnapshot %}