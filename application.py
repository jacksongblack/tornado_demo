# coding=utf-8

import urls
import tornado.web
import os.path
import config

SETTINGS = dict(
    template_path=config.TEMPLATE_DIR,
    static_path=config.STATIC_DIR,
)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls
        settings = SETTINGS
        tornado.web.Application.__init__(self, handlers, **settings)
