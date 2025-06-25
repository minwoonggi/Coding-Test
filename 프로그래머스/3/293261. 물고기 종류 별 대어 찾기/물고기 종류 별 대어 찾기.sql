-- 코드를 작성해주세요
select i.id, t.fish_name ,t.length from fish_info i join 
fish_name_info k on i.fish_type=k.fish_type join
(select n.fish_name as FISH_NAME, max(i.length) as LENGTH from fish_info i join fish_name_info n 
 on i.fish_type = n.fish_type
group by n.fish_name) t on k.fish_name=t.fish_name where i.length= t.length;