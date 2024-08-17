
    
    

select
    id as unique_field,
    count(*) as n_records

from read_csv('./jaffle-data/raw_customers.csv', names=['id', 'name'])
where id is not null
group by id
having count(*) > 1


