import platform
from os.path import dirname, abspath, join
from environs import Env
from loguru import logger

env = Env()
env.read_env()

# definition of flags
IS_WINDOWS = platform.system().lower() == 'windows'

# definition of dirs
ROOT_DIR = dirname(dirname(abspath(__file__)))
LOG_DIR = join(ROOT_DIR, env.str('LOG_DIR', 'logs'))

# definition of environments
DEV_MODE, TEST_MODE, PROD_MODE = 'dev', 'test', 'prod'
APP_ENV = env.str('APP_ENV', DEV_MODE).lower()
APP_DEBUG = env.bool('APP_DEBUG', True if APP_ENV == DEV_MODE else False)
APP_DEV = IS_DEV = APP_ENV == DEV_MODE
APP_PROD = IS_PROD = APP_DEV == PROD_MODE
APP_TEST = IS_TEST = APP_ENV = TEST_MODE

# redis host
REDIS_HOST = env.str('REDIS_HOST', '127.0.0.1')
# redis port
REDIS_PORT = env.int('REDIS_PORT', 6379)
# redis password, if no password, set it to None
REDIS_PASSWORD = env.str('REDIS_PASSWORD', None)
# redis connection string, like redis://[password]@host:port or rediss://[password]@host:port
REDIS_CONNECTION_STRING = env.str('REDIS_CONNECTION_STRING', None)

# definition of api
API_HOST = env.str('API_HOST', '0.0.0.0')
API_PORT = env.int('API_PORT', 5555)
API_THREADED = env.bool('API_THREADED', True)

# definition of flags
ENABLE_TESTER = env.bool('ENABLE_TESTER', True)
ENABLE_GETTER = env.bool('ENABLE_GETTER', True)
ENABLE_SERVER = env.bool('ENABLE_SERVER', True)

# logger
logger.add(env.str('LOG_RUNTIME_FILE', 'runtime.log'), level='DEBUG', rotation='1 week', retention='20 days')
logger.add(env.str('LOG_ERROR_FILE', 'error.log'), level='ERROR', rotation='1 week')
