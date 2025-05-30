with grp_number as (
select *, 
row_number() over(order by visit_date) as rn,
id - row_number() over(order by visit_date) as grp
from Stadium
where people > 99)
select id, visit_date, people from grp_number
where grp in (
select grp from grp_number
group by grp
having count(*) >= 3);