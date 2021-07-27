import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.set_default_header()

    def set_default_header(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")

    def options(self):
        pass