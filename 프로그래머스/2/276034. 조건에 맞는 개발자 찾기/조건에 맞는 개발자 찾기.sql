-- 코드를 작성해주세요
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME FROM DEVELOPERS
WHERE SKILL_CODE & (select CODE from skillcodes where NAME="Python")>0 
OR SKILL_CODE & (select CODE from skillcodes where NAME="C#")>0  order by id asc;