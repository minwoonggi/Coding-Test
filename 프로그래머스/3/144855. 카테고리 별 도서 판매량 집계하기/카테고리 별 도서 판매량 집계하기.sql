-- 코드를 입력하세요
 select p.CATEGORY, sum(c.TOTAL_SALES) from BOOK p
 join (SELECT book_id,sales_date, sum(sales) as TOTAL_SALES from book_sales
 where date_format(SALES_DATE,"%Y-%m") ="2022-01" group by book_id) c
 on p.book_id = c.book_id where date_format(SALES_DATE,"%Y-%m") ="2022-01" 
 group by p.category order by p.category asc;
