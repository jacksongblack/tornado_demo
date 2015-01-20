# coding=utf-8
import tornado.ioloop
import tornado.httpserver
import config

from application import Application

from tornado.options import define, options

define("port", default=config.ADDRESS.get('port'), help="run on the given port", type=int)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    print(''.join(('server run  port on ', options.port)))
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    import sys, unittest2
    import config

    if sys.argv[1] in "run":
        main()
    elif sys.argv[1] in "test":
        suite = unittest2.TestLoader().discover(config.TEST_DIR, pattern='test_*.py')
        unittest2.TextTestRunner(verbosity=2).run(suite)