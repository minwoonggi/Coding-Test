select p.PRODUCT_CODE, t.sales * p.price as SALES from  PRODUCT p join (SELECT p.PRODUCT_CODE, sum(s.sales_amount) as  SALES
 from PRODUCT p join OFFLINE_SALE s on p.PRODUCT_ID = s.PRODUCT_ID group by p.PRODUCT_CODE) t 
 on p.PRODUCT_CODE = t.PRODUCT_CODE
 order by sales desc, p.PRODUCT_CODE asc;