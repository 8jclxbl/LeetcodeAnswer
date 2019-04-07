-- My answer
SELECT d2.Id FROM Weather d1 LEFT JOIN Weather d2 ON DATEDIFF(d1.RecordDate,d2.RecordDate) = -1 AND d2.Temperature > d1.Temperature WHERE d2.Id IS NOT NULL;

-- Best answer
select wt1.Id
from Weather wt1,Weather wt2
where wt1.Temperature > wt2.Temperature AND TO_DAYS(wt1.RecordDate)-TO_DAYS(wt2.RecordDate)=1;