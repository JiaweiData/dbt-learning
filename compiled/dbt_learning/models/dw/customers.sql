select
    id as customer_id,
    name as customer_name
from read_csv('./jaffle-data/raw_customers.csv', names=['id', 'name'])