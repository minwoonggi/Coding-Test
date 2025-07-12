select c.id as ID from ECOLI_DATA c join 
ECOLI_DATA p on c.parent_id = p.id join ECOLI_DATA pp on p.parent_id = pp.id where pp.parent_id is null 
order by ID asc;