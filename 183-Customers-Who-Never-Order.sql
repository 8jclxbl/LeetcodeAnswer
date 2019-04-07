-- My answer
SELECT Name AS Customers From Customers c WHERE c.Id NOT IN (SELECT CustomerId From Orders);

-- Best answer
SELECT Name AS Customers
FROM Customers c
	LEFT JOIN Orders o ON c.Id = o.CustomerId
WHERE o.CustomerId IS NULL;