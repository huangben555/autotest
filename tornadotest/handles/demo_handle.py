import json
import sys

sys.path.append('C:\\PycharmProjects\\autoTest')

from tornadotest.intergration.logHandle import NbLog
from tornado.httpclient import AsyncHTTPClient
from tornadotest.handles.main_handle import MainHandler


class Handler(MainHandler):

    async def post(self):
        client = AsyncHTTPClient()
        response = await client.fetch("http://www.mockbin.com/har")
        NbLog().info(json.loads(response.body))
        self.finish(response.body)
