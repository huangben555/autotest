import tornado.web
import tornado.ioloop
import json, time
from intergration.logHandle import NbLog
from tornado.httpclient import AsyncHTTPClient
from handles.handle_demo import Handler


class BlockHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.set_default_header()

    def prepare(self):
        if self.request.method == "POST":
            request_data = self.request.body
            NbLog().info(request_data)

    def set_default_header(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS, DELETE")

    def post(self):
        self.finish(json.dumps({"Status": "OK"}))

    def options(self):
        pass


app = tornado.web.Application([
    (r"^/login/", Handler),
    (r"^/block/", BlockHandler),
])

app.listen(9999)

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().start()
