select * from (select CASE WHEN (SKILL_CODE & (select sum(CODE) from SKILLCODES where CATEGORY ="Front End" )) > 0 and 
(SKILL_CODE & (select code from SKILLCODES where NAME="Python"))>0
then "A" WHEN (SKILL_CODE & (select code from SKILLCODES where NAME="C#"))>0
then "B" when SKILL_CODE & (select sum(CODE) from SKILLCODES where CATEGORY ="Front End" ) then "C"
end as GRADE , ID, EMAIL
from DEVELOPERS) as t where t.grade is not null order by t.grade, t.id;