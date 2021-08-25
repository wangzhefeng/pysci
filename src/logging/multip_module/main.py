#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import logging.config

logging.config.fileConfig("logging.conf")

# root
root_logger = logging.getLogger("root")

# start root logger
root_logger.debug("test root logger...")

# main 
logger = logging.getLogger("main")
logger.info("test main logger")
logger.info("start import module 'mod'...")
import mod
logger.debug("let's test mod.testLogger()")
mod.testLogger()

# end root logger
root_logger.info("finish test...")