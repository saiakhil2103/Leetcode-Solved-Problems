with direct_reportees_count as (
    select e1.id as id, e1.name as name, e2.managerId as managerId
    from Employee e1
    inner join Employee e2
    where e1.id = e2.managerId
)
select e1.name 
from direct_reportees_count e1 
group by e1.managerId 
having count(e1.managerId) >= 5;