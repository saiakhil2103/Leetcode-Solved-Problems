-- select d.name as Department, e.name as Employee, e.salary as Salary 
-- from (
--     select *, rank() over (partition by departmentId order by salary desc) rnk from Employee
-- ) e 
-- left join Department d 
-- on e.departmentId = d.id
-- where e.rnk = 1;

select dept.name as Department,
    emp.name as Employee,
    emp.salary as Salary
from Department dept, Employee emp 
where emp.departmentId = dept.id and (emp.departmentId, emp.salary) in 
(select departmentId, max(salary) from Employee group by departmentId);