# coding=utf-8
import tornado.ioloop
import tornado.httpserver

from application import Application

from tornado.options import define, options
import config

define("port", default=config.ADDRESS.get('port'), help="run on the given port", type=int)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    print("server on")
    tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
    main()
