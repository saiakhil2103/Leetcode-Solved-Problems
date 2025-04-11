-- with cte as 
-- (SELECT name, Orders.customerId as cid FROM Customers LEFT JOIN Orders ON Customers.id = Orders.customerId)
-- select name as Customers from cte where cid is null;


select name as Customers from Customers where id not in (select customerId from Orders);