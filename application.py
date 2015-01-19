# coding=utf-8

import urls
import tornado.web
import config

SETTINGS = dict(
    template_path=config.TEMPLATE_DIR,
    static_path=config.STATIC_DIR,
    cookie_secret=config.COOKIE_SECRET,
    xsrf_cookie=config.XSRF_COOKIE
)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls.urls
        settings = SETTINGS
        super(Application, self).__init__(handlers, **settings)
