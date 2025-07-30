WITH RECURSIVE  clock as (
    select 0 as hour
    
    union all
    
    select hour+1 from clock where hour<23
)
select o.HOUR, CASE WHEN t.COUNT IS NULL THEN 0 ELSE t.COUNT end as COUNT  from clock o left join (select  HOUR(DATETIME) as hour ,count(*) as COUNT from ANIMAL_OUTS group by HOUR(DATETIME)) as t on o.hour = t.hour;