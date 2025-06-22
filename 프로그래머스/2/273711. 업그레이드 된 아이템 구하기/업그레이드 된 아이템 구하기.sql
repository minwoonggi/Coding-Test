-- 코드를 작성해주세요
select ITEM_ID,ITEM_NAME,RARITY from item_info
where item_id in (select tree.item_id from item_info info join item_tree tree on info.item_id = tree.parent_item_id
where info.rarity="rare"
AND tree.PARENT_ITEM_ID IS NOT NULL) order by item_id desc;

