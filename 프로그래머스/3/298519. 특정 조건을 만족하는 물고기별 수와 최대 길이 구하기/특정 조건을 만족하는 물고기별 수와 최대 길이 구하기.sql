select count(*) as FISH_COUNT,max(t.LENGTH) as MAX_LENGTH, t.FISH_TYPE from 
(select CASE WHEN (LENGTH is null or LENGTH <=10) then 10 
 else LENGTH end as "LENGTH", ID,FISH_TYPE	,TIME
 from FISH_INFO) as t 
group by t.FISH_TYPE having avg(t.LENGTH)>=33 
order by t.FISH_TYPE ; 
