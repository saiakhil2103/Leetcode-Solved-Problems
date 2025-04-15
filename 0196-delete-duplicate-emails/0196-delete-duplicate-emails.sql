-- delete p1 from person p1, person p2
-- where p1.email = p2.email 
-- and p1.id > p2.id;

-- delete p from Person p
-- join Person p2 
-- on p.email = p2.email and p.id > p2.id;

-- delete from Person
-- where id not in (
--     select * from (select min(id) from Person group by email) a
-- )

delete
  from Person
  where id not in (select * from (SELECT MIN(id) 
  FROM Person GROUP BY email) a )