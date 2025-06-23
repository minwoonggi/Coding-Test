-- 코드를 작성해주세요
select p.id,count(c.parent_id) as child_count from ECOLI_DATA c right join ECOLI_DATA p on c.PARENT_ID = p.id group by p.id;