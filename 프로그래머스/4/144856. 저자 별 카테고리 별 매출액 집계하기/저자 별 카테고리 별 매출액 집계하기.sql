-- 코드를 입력하세요
select a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, sum(sales.sales*b.price) as TOTAL_SALES from
BOOK b join AUTHOR a on b.AUTHOR_ID=a.AUTHOR_ID join 
(SELECT BOOK_ID, SUM(SALES) as sales from BOOK_SALES 
 where DATE_FORMAT(SALES_DATE,"%Y-%m")="2022-01" group by book_id) sales
 on sales.BOOK_ID=b.BOOK_ID group by b.category , a.author_name order by a.AUTHOR_ID asc ,b.CATEGORY desc;
