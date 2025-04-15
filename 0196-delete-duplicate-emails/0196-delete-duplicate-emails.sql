-- delete p1 from person p1, person p2
-- where p1.email = p2.email 
-- and p1.id > p2.id;

delete p from Person p
join Person p2 
on p.email = p2.email and p.id > p2.id;