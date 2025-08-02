SELECT YEAR(sale.SALES_DATE) as YEAR,
MONTH(sale.SALES_DATE) as MONTH,
info.GENDER,
count(distinct sale.user_id) as USERS
from ONLINE_SALE sale join USER_INFO info on sale.USER_ID=info.USER_ID 
where info.GENDER IS NOT NULL
group by YEAR(sale.SALES_DATE),MONTH(sale.SALES_DATE) ,info.GENDER
order by YEAR(sale.SALES_DATE) asc ,MONTH(sale.SALES_DATE) asc ,info.GENDER asc;