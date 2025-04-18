-- SELECT email FROM Person
-- GROUP BY email 
-- HAVING count(email) > 1;

-- SELECT DISTINCT(p1.email) FROM Person p1, Person p2
-- WHERE p1.id <> p2.id AND p1.email = p2.email;

SELECT DISTINCT(p1.email) FROM Person p1 JOIN Person p2 
ON p1.email = p2.email AND p1.id <> p2.id;