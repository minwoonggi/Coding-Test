-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, SUM(TOTAL_ORDER) as TOTAL_ORDER from first_half f join icecream_info i on f.flavor = i.flavor 
group by ingredient_type ORDER BY TOTAL_ORDER ASC;