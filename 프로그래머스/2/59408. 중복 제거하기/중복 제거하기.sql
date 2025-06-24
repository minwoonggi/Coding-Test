-- 코드를 입력하세요
select count(*) as count from (select count(*) from animal_ins where name is not null group by name) as t;