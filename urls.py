# coding=utf-8
# 项目路由配置
import handlers

urls = [
    (r'/user', handlers.UserHandler),
    (r'/room', handlers.RoomWebHandler),
    (r'/websocket', handlers.ChatHandler),
]
