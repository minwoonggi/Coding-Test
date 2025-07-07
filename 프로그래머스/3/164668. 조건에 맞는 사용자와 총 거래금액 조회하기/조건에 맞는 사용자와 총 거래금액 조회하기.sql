select p.USER_ID , p.NICKNAME , c.TOTAL_SALES FROM USED_GOODS_USER p join 
(SELECT sum(price) as TOTAL_SALES,writer_id from USED_GOODS_BOARD where status = "DONE"
group by writer_id having TOTAL_SALES>=700000) c on p.user_id=c.writer_id 
order by c.total_sales asc;