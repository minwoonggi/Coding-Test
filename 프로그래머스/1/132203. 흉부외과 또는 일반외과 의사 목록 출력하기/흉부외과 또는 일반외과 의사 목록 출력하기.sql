-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD,"%Y-%m-%d") FROM DOCTOR where MCDP_CD= "CS" OR mcdp_cd = "GS"
order by hire_ymd desc, dr_name asc;