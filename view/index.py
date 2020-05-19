import tornado.web
import json
import mytoken
from model import model


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        data = json.loads(self.request.body)
        if data['user'] == 'admin' and data['psw'] == '123456':
            t = mytoken.Token(data).token
            model.Book.create_table()
            book = model.Book(user=data['user'], psw=data['psw'], token=t)
            book.save()
            print('ok')


class AdminHandler(tornado.web.RequestHandler):
    def post(self):
        data = self.request.body.decode("utf8")
        res = model.Book.get(user='admin')
        print('shkjgkhgjdfasda')
