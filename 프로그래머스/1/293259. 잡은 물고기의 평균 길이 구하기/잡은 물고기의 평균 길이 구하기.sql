-- 코드를 작성해주세요

select round(avg(c.length),2) as AVERAGE_LENGTH from FISH_INFO p join
(select id,coalesce(length, 10) as length from FISH_INFO) c on p.id=c.id;