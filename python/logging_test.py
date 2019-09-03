#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging 
logging.basicConfig(filename = "F:/personal/script/log/test.log",
                    filemode = "w",
                    format = "[%(asctime)s] 【%(name)s:%(levelname)s】: %(message)s", 
                    datefmt="%Y-%m-%d %H:%M:%S",
                    style = "%",
                    level = "DEBUG",
                    # stream = "",
                    # handles = ""
                    )

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
try:
    a = 5
    b = 0
    c = a / b
except ZeroDivisionError as e:
    logging.exception("Exception occurred")
    logging.error("Exception occurred", 
                  exc_info = True)
    logging.log(level = logging.DEBUG, 
                msg = "Exception occurred", 
                exc_info = True)


