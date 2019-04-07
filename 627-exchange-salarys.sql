-- My answer
 UPDATE salary SET sex = CASE WHEN sex = "m" THEN "f" ELSE "m" END;

 -- Best answer
 UPDATE salary SET sex = IF(sex = 'm', 'f', 'm');