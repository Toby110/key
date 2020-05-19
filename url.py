import tornado.web
import config
from view import index
from view import admin

def make_app():
        return tornado.web.Application([
            (r'/', index.IndexHandler),
            (r'/admin',index.AdminHandler),
            (r'/login', admin.LoginHandler),
         ], **config.settings)
