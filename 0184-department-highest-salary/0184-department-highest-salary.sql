select d.name as Department, e.name as Employee, e.salary as Salary 
from (
    select *, rank() over (partition by departmentId order by salary desc) rnk from Employee
) e 
left join Department d 
on e.departmentId = d.id
where e.rnk = 1;