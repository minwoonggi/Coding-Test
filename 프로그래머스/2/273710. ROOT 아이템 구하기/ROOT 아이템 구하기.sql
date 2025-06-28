-- 코드를 작성해주세요
select info.ITEM_ID, info.ITEM_NAME from ITEM_INFO info join ITEM_TREE tree on 
info.item_id = tree.item_id where PARENT_ITEM_ID is null order by  info.ITEM_ID asc;