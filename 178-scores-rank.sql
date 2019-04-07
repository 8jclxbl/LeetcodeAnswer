-- 无法处理单行时出现的问题
SELECT Score,CAST(`Rank` AS UNSIGNED INTEGER) AS `RANK` FROM (SELECT Score, 
IF (@prevRank = Score, @curRank, @curRank := @curRank + 1) AS `Rank`,
@prevRank := Score
FROM Scores s,
(SELECT @curRank := 0, @prevRank := 0) r
ORDER BY Score DESC) t;

select Score, 
(select count(distinct(Score)) from Scores 
where Score >= s.Score) Rank  
from Scores s order by Score DESC;  

-- Best answer
SELECT Score, 
	CASE	
    WHEN @score = obj.Score THEN  cast(@rank as SIGNED)
	WHEN @score := obj.Score THEN @rank := @rank + 1 
    WHEN @score = 0 THEN  @rank := @rank + 1	
	END AS Rank 
	FROM ( 
			select * 
			from Scores Order by Score+0 DESC 
	) obj, (SELECT @rank := 0 ,@score := null) r 