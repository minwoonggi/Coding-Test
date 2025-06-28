-- 코드를 작성해주세요

select info.item_id, info.ITEM_NAME ,info.RARITY from ITEM_TREE tree right join ITEM_INFO info on tree.PARENT_ITEM_ID = info.ITEM_ID
where tree.PARENT_ITEM_ID is null order by info.item_id desc;