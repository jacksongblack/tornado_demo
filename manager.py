# coding=utf-8
import sys, os;

print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend([os.path.dirname(__file__)])

import tornado.ioloop
import tornado.httpserver
import config
import logging
import signal
import time

from application import Application

from tornado.options import define, options

MAX_WAIT_SECONDS_BEFORE_SHUTDOWN = 3

define("port", default=config.ADDRESS.get('port'), help="run on the given port", type=int)


def sig_handler(sig, frame):
    logging.warning('Caught signal: %s', sig)
    tornado.ioloop.IOLoop.instance().add_callback(shutdown)


def shutdown():
    logging.info('Stopping http server')
    server.stop()

    logging.info('Will shutdown in %s seconds ...', MAX_WAIT_SECONDS_BEFORE_SHUTDOWN)
    io_loop = tornado.ioloop.IOLoop.instance()

    deadline = time.time() + MAX_WAIT_SECONDS_BEFORE_SHUTDOWN

    def stop_loop():
        now = time.time()
        if now < deadline and (io_loop._callbacks or io_loop._timeouts):
            io_loop.add_timeout(now + 1, stop_loop)
        else:
            io_loop.stop()
            logging.info('Shutdown')

    stop_loop()


def main():
    global server
    tornado.options.parse_command_line()

    server = tornado.httpserver.HTTPServer(Application())
    server.listen(options.port)
    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)
    logging.info("start server on port %s" % (options.port,))
    tornado.ioloop.IOLoop.instance().start()
    logging.info("Exit...")


if __name__ == "__main__":
    import sys, unittest2

    try:
        if sys.argv[1] in "run":
            main()


        elif sys.argv[1] in "test":
            suite = unittest2.TestLoader().discover(config.TEST_DIR, pattern='test_*.py')
            unittest2.TextTestRunner(verbosity=2).run(suite)
    except IndexError:
        print("Usage: 1.python runserver run  start on server starting \n"
              "       2.python manager.py test on testing  ")
