#pylint:disable=undefined-variable,wildcard-import,no-name-in-module
from adafruit_logger import *
logger = Logger()

logger.level = ERROR
logger.log(INFO, 'Info message')
logger.log(ERROR, 'Error message')
