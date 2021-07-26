import tornado.web
import tornado.ioloop
import json, time
import sys

sys.path.append('C:\\PycharmProjects\\autoTest')

from tornadotest.intergration.logHandle import NbLog
from tornado.httpclient import AsyncHTTPClient


class Handler(tornado.web.RequestHandler):

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

    async def post(self):
        client = AsyncHTTPClient()
        response = await client.fetch("http://www.mockbin.com/har")
        NbLog().info(json.loads(response.body))
        self.finish(response.body)

    def options(self):
        pass