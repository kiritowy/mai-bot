#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict
from doctest import master

import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot
# from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter


# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
# nonebot.load_builtin_plugins()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
# driver.register_adapter(ONEBOT_V11Adapter)

driver.config.help_text = {}


nonebot.load_plugins("src/plugins")
# nonebot.load_plugins("src/plugins/nonebot_plugin_admin_a")
# nonebot.load_plugin('nonebot_plugin_arcaea')
nonebot.load_plugin("nonebot_plugin_youthstudy")
# nonebot.load_plugin("nonebot_plugin_test")
# nonebot.load_plugins("nonebot_plugin_gamedraw")
# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...


if __name__ == "__main__":
    nonebot.run(app="bot:app")
    # nonebot.run(app="__mp_main__:app")


