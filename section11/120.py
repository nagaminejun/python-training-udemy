"""
CRITICAL:root:critical
ERROR:root:error
WARNING:root:warning
INFO:root:info test
INFO:root:info test test2!
DEBUG:root:debug
"""

import logging

# formatter = '%(levelname)s:%(message)s'
# formatter = '%(asctime)s:%(message)s'
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.INFO, format=formatter)
# logging.basicConfig(filename='test.log', level=logging.DEBUG)


# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.info('info %s', 'test')
# logging.info('info %s %s', 'test', 'test2!')
# logging.debug('debug')

# 121
logging.basicConfig(level=logging.INFO)
logging.info('info')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('debug')
