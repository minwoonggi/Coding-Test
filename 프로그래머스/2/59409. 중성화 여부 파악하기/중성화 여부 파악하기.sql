SELECT ANIMAL_ID, NAME, 
CASE WHEN SEX_UPON_INTAKE like "Neutered%" or SEX_UPON_INTAKE like "Spayed%" then "O"
else "X" end as "중성화" 
FROM ANIMAL_INS order by ANIMAL_ID asc;