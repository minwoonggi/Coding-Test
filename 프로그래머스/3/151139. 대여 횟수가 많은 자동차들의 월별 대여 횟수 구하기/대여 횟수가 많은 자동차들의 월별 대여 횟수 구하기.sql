SELECT MONTH(START_DATE) as MONTH,
       c.CAR_ID, 
       count(*) as RECORDS 
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY c 
JOIN (
    SELECT car_id 
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY where month(start_date) >=8 and month(start_date)<=10
    GROUP BY car_id 
    HAVING count(*) >= 5
) j ON c.car_id = j.car_id where month(c.START_DATE) >=8 and  month(c.START_DATE)<=10
GROUP BY MONTH(START_DATE), c.car_id
ORDER BY MONTH(START_DATE) ASC, c.car_id DESC;