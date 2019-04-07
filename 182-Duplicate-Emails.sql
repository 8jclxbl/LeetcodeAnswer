-- Best answer
select lower(Email) as Email  from Person group by Email having count(*) > 1;

-- My answer
 SELECT Email FROM (SELECT Email,COUNT(Email) AS ecount FROM Person GROUP BY Email) AS Ecount WHERE ecount > 1;