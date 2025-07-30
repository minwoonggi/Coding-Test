select ID,EMAIL,FIRST_NAME,LAST_NAME from DEVELOPERS where skill_code & (select sum(code) from SKILLCODES where CATEGORY ="Front End") order by id;
## 비트마스크 합산?