import logging
import logtest  # 上で作ったファイルをインポート

# 基本的なログ設定（コンソール出力用）
logging.basicConfig(level=logging.INFO)

class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message

# メイン側のロガーを作成
logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())
logger.info('from main')
logger.info('from main password = "testpass"')

# 別のモジュールの関数を呼び出す
logtest.do_something()
