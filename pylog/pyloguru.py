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