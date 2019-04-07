select distinct
    l1.Num as ConsecutiveNums
from
    Logs as l1,Logs as l2,Logs as l3
where
    l1.Num = l2.Num and l2.Num = l3.Num and l1.Id = l2.Id -1 and l2.Id = l3.Id -1


SELECT t1.Num as ConsecutiveNums
FROM logs AS t1, logs AS t2, logs AS t3
WHERE t1.Id = t2.Id-1 and t2.Id = t3.Id-1 and t1.Num = t2.Num and t2.Num = t3.Num
GROUP BY t1.Num;


SELECT x.Num as ConsecutiveNums FROM
(SELECT y.Num , SUM(INDEXS) FROM
    (SELECT Num,
    CASE WHEN @preNum = t.Num then @index else @index := 1
    END AS INDEXS,
    @index := @index+1,
    @preNum := t.Num
    FROM Logs t,
    (SELECT@preNum := null, @index := 1) dse)y
WHERE y.INDEXS > 2
GROUP BY y.Num)x

SELECT
	DISTINCT temp1.b AS 'ConsecutiveNums'
FROM
	(
		SELECT
			num AS 'b',
			@i :=
		IF (@s = num ,@i + 1, 1) AS 'a',
		@s := num
	FROM
		LOGS,
		(SELECT @i := 1 ,@s := NULL) t
	) temp1
WHERE
	temp1.a >= 3