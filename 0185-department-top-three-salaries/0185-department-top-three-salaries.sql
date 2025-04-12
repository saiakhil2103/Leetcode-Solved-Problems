select dept_name as Department, emp_name as Employee, emp_salary as Salary
from (
    select dept.name as dept_name, 
        emp.name as emp_name,
        emp.salary as emp_salary, 
        dense_rank() over(partition by departmentId order by salary desc) as d_rank
    from Employee emp 
    inner join Department dept
    on emp.departmentId = dept.id
) T
where d_rank <= 3;