-- 코드를 입력하세요
select p.CAR_ID, CASE WHEN MAX(CASE WHEN c.AVAILABILITY ="대여중" then 1 ELSE 0 end)>0 then "대여중" else "대여 가능" end as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY p join
(SELECT car_id , case when start_date<="2022-10-16" and end_date>="2022-10-16" 
then "대여중" else "대여 가능" end as "AVAILABILITY"
from CAR_RENTAL_COMPANY_RENTAL_HISTORY) c on p.car_id= c.car_id group by car_id order by p.car_id desc;