# -*- coding: utf-8 -*-


# ***************************************************
# * File        : main.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-06-30
# * Version     : 0.1.063023
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


import logging
import logging.config


# --------
# log config
# --------
logging.config.fileConfig("logging.conf")

# --------
# root
# --------
root_logger = logging.getLogger("root")
# start root logger
root_logger.debug("test root logger...")
# --------
# main
# --------
logger = logging.getLogger("main")
logger.info("test main logger")
logger.info("start import module 'mod'...")
import mod
logger.debug("let's test mod.testLogger()")
mod.testLogger()
# end root logger
root_logger.info("finish test...")
