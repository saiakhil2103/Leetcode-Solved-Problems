-- select e1.name as Employee from Employee e1 where e1.salary > (select e2.salary from Employee e2 where e1.salary > e2.salary and e1.managerId = e2.id);

SELECT e2.name as Employee
FROM employee e1
INNER JOIN employee e2 ON e1.id = e2.managerID
WHERE
e1.salary < e2.salary