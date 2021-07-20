import tornado.web
import tornado.ioloop
import json


class Handler(tornado.web.RequestHandler):

    def initialize(self):
        self.set_default_header()

    def set_default_header(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'Content-Type')

    def post(self):
        print('request successfully')
        self.finish(json.dumps({"Status": 'OK'}))

    def options(self):
        pass


app = tornado.web.Application([
    (r'^/login/', Handler)
])

app.listen(9999)

tornado.ioloop.IOLoop.current().start()
