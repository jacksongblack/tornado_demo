from core.handle import BaseHandler
from model.user import User


class UserHandler(BaseHandler):
    def get(self):
        self.render('user/login.html', user=User().get(id=150105204803891224000001))