import tornado.web


class UserHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('user/login.html')