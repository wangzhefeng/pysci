

## logging


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import sys
from os import makedirs
from os.path import dirname, exists
from cmreslogging.handlers import CMRESHandler

loggers = {}

LOG_ENABLED = True     # 是否开启日志
LOG_TO_CONSOLE = True  # 是否输出到控制台
LOG_TO_FILE = True     # 是否输出到文件
LOG_TO_ES = True       # 是否输出到 Elasticsearch

LOG_PATH = './runtime.log'        # 日志文件路径
LOG_LEVEL = 'DEBUG'               # 日志级别
LOG_FORMAT = '%(levelname)s - \
              %(asctime)s - \
              process: %(process)d - \
              %(filename)s - %(name)s - \
              %(lineno)d - %(module)s - \
              %(message)s'        # 每条日志输出格式
ELASTIC_SEARCH_HOST = 'eshost'    # Elasticsearch Host
ELASTIC_SEARCH_PORT = 9200        # Elasticsearch Port
ELASTIC_SEARCH_INDEX = 'runtime'  # Elasticsearch Index Name
APP_ENVIRONMENT = 'dev'           # 运行环境，如测试环境还是生产环境

def get_logger(name=None):
    """
    get logger by name
    :param name: name of logger
    :return: logger
    """
    global loggers

    if not name: name = __name__

    if loggers.get(name):
        return loggers.get(name)

    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    # 输出到控制台
    if LOG_ENABLED and LOG_TO_CONSOLE:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(level=LOG_LEVEL)
        formatter = logging.Formatter(LOG_FORMAT)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    # 输出到文件
    if LOG_ENABLED and LOG_TO_FILE:
        # 如果路径不存在，创建日志文件文件夹
        log_dir = dirname(log_path)
        if not exists(log_dir): makedirs(log_dir)
        # 添加 FileHandler
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(level=LOG_LEVEL)
        formatter = logging.Formatter(LOG_FORMAT)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # 输出到 Elasticsearch
    if LOG_ENABLED and LOG_TO_ES:
        # 添加 CMRESHandler
        es_handler = CMRESHandler(hosts=[{'host': ELASTIC_SEARCH_HOST, 'port': ELASTIC_SEARCH_PORT}],
                                  # 可以配置对应的认证权限
                                  auth_type=CMRESHandler.AuthType.NO_AUTH,  
                                  es_index_name=ELASTIC_SEARCH_INDEX,
                                  # 一个月分一个 Index
                                  index_name_frequency=CMRESHandler.IndexNameFrequency.MONTHLY,
                                  # 额外增加环境标识
                                  es_additional_fields={'environment': APP_ENVIRONMENT}  
                                  )
        es_handler.setLevel(level=LOG_LEVEL)
        formatter = logging.Formatter(LOG_FORMAT)
        es_handler.setFormatter(formatter)
        logger.addHandler(es_handler)

    # 保存到全局 loggers
    loggers[name] = logger
    return logger


```


## loguru

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loguru import logger

def main():
    trace = logger.add("runtime.log",
                 format = "{time} {level} {message}", 
                 filter = "my_module", 
                 level = "INFO",
                 rotation = "500 MB",
                 # rotation = "00:00",
                 # rotation = "1 week",
                 retention = "10 days",
                 compression = "zip")
    logger.debug("this is a debug message")
    logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature = 'f - strings')
    # 删除添加的 sink，重新刷新 log 文件并写入新的内容
    # logger.remove(trace)
    logger.debug("this is another debug message")

    @logger.catch
    def myFucntion(x, y, z):
        return 1 / (x, y, z)

    myFucntion(0, 0, 0)

if __name__ == "__main__":
    main()
```