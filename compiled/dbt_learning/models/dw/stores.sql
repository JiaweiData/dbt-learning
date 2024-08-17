select
    stores.id as store_id,
    stores.name as store_name,
    sm.user_id as store_manager_id,
    customers.customer_name as store_manager_name,
    stores.opened_at,
    
    cast(stores.tax_rate as numeric(12,4))
 as tax_rate
from read_csv('./jaffle-data/raw_stores.csv', names=['id','name','opened_at','tax_rate']) as stores
    left join "dev"."main"."store_manager" as sm on stores.id = sm.store_id
    left join "dev"."main"."customers" as customers on sm.user_id = customers.customer_id