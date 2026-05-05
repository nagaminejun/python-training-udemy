import logging

# このファイル専用のロガーを作成（__name__ は "logtest" になる）
logger = logging.getLogger('logger_simpleExample')
logger.setLevel(logging.DEBUG)

# ファイルに出力するための設定（FileHandler）
h = logging.FileHandler('logtest.log')
logger.addHandler(h)

def do_something():
    # 各レベルでログを出力
    logger.info('from logtest info')
    logger.info('from logtest')
    logger.debug('from logtest debug')

# 結果
# INFO:__main__:from main
# INFO:logtest:from logtest info
# INFO:logtest:from logtest
# DEBUG:logtest:from logtest debug
