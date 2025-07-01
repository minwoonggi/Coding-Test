select p.CATEGORY,c.price as MAX_PRICE, p.PRODUCT_NAME from FOOD_PRODUCT p join
(SELECT CATEGORY,max(PRICE) as PRICE from FOOD_PRODUCT group by CATEGORY) c on
p.price=c.price and p.CATEGORY = c.CATEGORY where p.CATEGORY = "과자" or
p.CATEGORY = "국" or p.CATEGORY = "김치" or p.CATEGORY = "식용유"
order by c.price desc;