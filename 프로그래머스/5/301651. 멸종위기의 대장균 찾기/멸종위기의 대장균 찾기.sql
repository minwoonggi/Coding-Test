with recursive genetable as (
    -- 시작점
    select id, parent_id, 1 as generation from ECOLI_DATA
    where parent_id is null
    union all
    -- 재귀
     select c.id, c.PARENT_ID, p.generation+1 from ECOLI_DATA c
    join genetable p on p.id = c.PARENT_ID
)


select count(*) as COUNT,GENERATION from genetable
where id not in (select parent_id from ECOLI_DATA where parent_id is not null)
group by generation
order by generation asc;