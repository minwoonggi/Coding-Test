select c.SCORE, p.EMP_NO, p.EMP_NAME, p.POSITION, p.EMAIL from HR_EMPLOYEES p join 
(select EMP_NO, sum(score) as SCORE from HR_GRADE where year = 2022 group by emp_no) c
on p.emp_no = c.emp_no order by c.SCORE desc limit 1;