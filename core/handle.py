import os

from tornado import web
import time
_app_cache = {}


class InstanceCache(object):
    def clear(self):
        global _app_cache

        for key, value in _app_cache.iteritems():
            expiry = value[1]
            if expiry and time() > expiry:
                del _app_cache[key]

    def flush_all(self):
        global _app_cache

        _app_cache = {}

    def set(self, key, value, seconds=0):
        global _app_cache

        if seconds < 0:
            seconds = 0

        _app_cache[key] = (value, time() + seconds if seconds else 0)

    def get(self, key):
        global _app_cache

        value = _app_cache.get(key, None)
        if value:
            expiry = value[1]
            if expiry and time() > expiry:
                del _app_cache[key]
                return None
            else:
                return value[0]
        return None

    def delete(self, key):
        global _app_cache
    
        if _app_cache.has_key(key):
            del _app_cache[key]
        return None

class BaseHandler(web.RequestHandler):
    @property
    def cache(self):
        return self.application.cache
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    pass
