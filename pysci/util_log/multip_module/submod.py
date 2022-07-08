# -*- coding: utf-8 -*-


import logging


logger = logging.getLogger("main.mod.submod")
logger.info("logger of submod say something...")


def test():
	logger.info("this is submod.tst()...")
