# -*- coding: utf-8 -*-

import Logger

logtest = Logger.Logger('test.log')

logtest.debug("This is a debug log...")
logtest.info("This is a info log...")
logtest.warn("This is a warning log...")
logtest.error("This is a error log...")
logtest.critical("This is a critical log...")
