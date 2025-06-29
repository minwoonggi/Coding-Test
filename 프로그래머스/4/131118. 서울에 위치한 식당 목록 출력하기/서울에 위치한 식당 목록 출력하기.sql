-- 코드를 입력하세요
select info.REST_ID, info.REST_NAME, info.FOOD_TYPE, info.FAVORITES	,info.ADDRESS, 
round(avg(review.REVIEW_SCORE),2) as SCORE
from (SELECT * from REST_INFO where ADDRESS like "서울%") info 
join REST_REVIEW review on info.REST_ID = review.REST_ID group by info.REST_ID
order by SCORE desc,FAVORITES desc ;