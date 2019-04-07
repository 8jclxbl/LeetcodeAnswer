-- My answer
-- SELECT class FROM (SELECT class,COUNT(class) AS cc FROM (SELECT calss FROM courses GROUP BY student) AS cl GROUP BY class) AS ccount WHERE cc >= 5;

-- Best answer
SELECT class from courses group by class having count(DISTINCT student) >= 5;