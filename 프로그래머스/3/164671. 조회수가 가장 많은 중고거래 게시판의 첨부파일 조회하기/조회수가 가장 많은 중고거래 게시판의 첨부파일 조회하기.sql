SELECT concat("/home/grep/src/",ugb.BOARD_ID,"/",ugf.FILE_ID,ugf.FILE_NAME,ugf.FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD ugb join USED_GOODS_FILE ugf
on ugb.BOARD_ID=ugf.BOARD_ID where ugb.views = (select MAX(views) from USED_GOODS_BOARD)
order by ugf.file_id desc;