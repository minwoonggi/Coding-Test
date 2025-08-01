select ROUTE, concat(ROUND(sum(D_BETWEEN_DIST),1),"km") as TOTAL_DISTANCE, 
concat(ROUND(avg(D_BETWEEN_DIST),2),"km") as AVERAGE_DISTANCE from SUBWAY_DISTANCE group by ROUTE
order by ROUND(sum(D_BETWEEN_DIST),1) desc;