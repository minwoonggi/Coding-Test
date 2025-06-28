-- 코드를 작성해주세요
select p.DEPT_ID, p.DEPT_NAME_EN, round(AVG(C.SAL)) as AVG_SAL from HR_DEPARTMENT p join HR_EMPLOYEES c on p.dept_id =c.dept_id
group by p.DEPT_NAME_EN,p.dept_id order by AVG_SAL desc;