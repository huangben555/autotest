import tornado.web
import tornado.ioloop
import json


class AddHandler(tornado.web.RequestHandler):

    def initialize(self):
        # self.request.method = 'POST'
        # print(self.request.method, type(self.request.method))
        self.set_default_header()

    def get(self):
        self.write("U get story id is ")

    def post(self):
        self.write(json.dumps({"sum": 'rrrrrr'}))

    def set_default_header(self):
        print("setting headers!!!")
        self.set_header('Access-Control-Allow-Origin', '*')
        # self.set_header('Access-Control-Allow-Origin', 'http://localhost:8080')
        # self.set_header('Access-Control-Allow-Headers', 'X-Requested-With')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH, OPTIONS')
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.set_header('Access-Control-Allow-Headers', 'Content-Type')

    def options(self):
        pass


app = tornado.web.Application([
    (r'^/login/$', AddHandler)
])

app.listen(9999)

tornado.ioloop.IOLoop.current().start()
