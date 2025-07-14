SELECT i.NAME,i.DATETIME from ANIMAL_OUTS o right join ANIMAL_INS i on i.ANIMAL_ID = o.ANIMAL_ID 
where o.DATETIME is null order by i.datetime asc limit 3;