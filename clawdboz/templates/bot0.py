#!/usr/bin/env python3
"""
嗑唠的宝子 - 飞书 Bot 启动脚本

这是 Bot 的入口文件，由 bot_manager.sh 调用启动。
你也可以直接运行: python bot0.py
"""
import os
from clawdboz import Bot

# 从环境变量或配置文件读取配置
bot = Bot(config_path="config.json")
bot.run()
