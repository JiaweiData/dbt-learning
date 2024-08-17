select
    stores.id as store_id,
    stores.name as store_name,
    sm.user_id as store_manager_id,
    customers.customer_name as store_manager_name,
    stores.opened_at,
    {{ dbt.cast("stores.tax_rate", api.Column.numeric_type('numeric', 12 ,4) )}} as tax_rate
from {{ source("jaf_csv", "stores") }} as stores
    left join {{ ref('store_manager') }} as sm on stores.id = sm.store_id
    left join {{ ref('customers') }} as customers on sm.user_id = customers.customer_id
