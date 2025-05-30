-- SELECT DISTINCT l1.num AS ConsecutiveNums 
-- FROM Logs l1, Logs l2, Logs l3
-- WHERE l1.id = l2.id - 1 AND l2.id = l3.id - 1 and l1.num = l2.num and l2.num = l3.num;

with cte as (
    select num, 
    lead(num, 1) over() num1,
    lead(num, 2) over() num2
    from logs
)
select distinct num as ConsecutiveNums from cte where num=num1 and num=num2;