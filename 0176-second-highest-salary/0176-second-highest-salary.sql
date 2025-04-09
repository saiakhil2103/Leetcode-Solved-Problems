-- select max(salary) as SecondHighestSalary from Employee where salary < (select max(salary) from Employee) limit 1;

select (select distinct salary from Employee order by salary desc limit 1 offset 1) as SecondHighestSalary; 