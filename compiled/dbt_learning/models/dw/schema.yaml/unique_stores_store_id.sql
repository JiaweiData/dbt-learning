
    
    

select
    store_id as unique_field,
    count(*) as n_records

from "dev"."main"."stores"
where store_id is not null
group by store_id
having count(*) > 1


