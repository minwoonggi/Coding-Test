-- 코드를 작성해주세요
select t.year as YEAR,t.max - x.size_of_colony as YEAR_DEV, x.ID from ecoli_data x join 
(select YEAR(DIFFERENTIATION_DATE) as year,max(size_of_colony) as max from ecoli_data group by YEAR(DIFFERENTIATION_DATE)) t on YEAR(x.DIFFERENTIATION_DATE)= t.year order by
t.year asc, YEAR_DEV asc ;