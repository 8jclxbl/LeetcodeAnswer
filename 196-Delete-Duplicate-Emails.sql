delete from Person
where Id not in (select Id from (
                        select min(Id) as Id 
                        from Person 
                        group by Email) as p
                );


-- My answer
delete e1 From Person e1 INNER JOIN Person e2 WHERE e1.Email = e2.Email AND e1.Id > e2.Id;