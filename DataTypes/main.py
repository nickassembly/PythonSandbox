import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
import helper
import logging.config
import traceback
from logging.handlers import RotatingFileHandler 

logging.config.fileConfig('logging.conf') # to you config file
logger2 = logging.getLogger('simpleExample')
logger2.debug('this is a debug message')

logger3 = logging.getLogger(__name__)
logger3.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc. 
handler2 = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger3.addHandler(handler2)

for _ in range(10000):
    logger3.info('Hello world')


# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')

try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True) # includes the stack trace in logger

try:
    a = [1,2,3]
    val = a[4]
except:
    logging.error('The error is %s", traceback.format_exc()')