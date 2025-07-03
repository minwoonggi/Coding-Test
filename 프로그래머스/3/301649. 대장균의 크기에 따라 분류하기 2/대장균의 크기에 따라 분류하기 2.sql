select c.ID, CASE WHEN c.rank <= c.total *0.25 then "CRITICAL"
when c.rank <= c.total*0.5 then "HIGH"
when c.rank<=c.total*0.75 then "MEDIUM"
ELSE "LOW" end
as COLONY_NAME from ECOLI_DATA p join
(select id,count(*) over() as total, row_number() over (order by size_of_colony desc) as `rank`
from ECOLI_DATA) c on p.id=c.id order by c.id asc;