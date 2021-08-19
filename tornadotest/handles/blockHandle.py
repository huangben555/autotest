import json
import sys

sys.path.append('C:\\PycharmProjects\\autoTest')

from tornadotest.intergration.logWriter import NbLog
from tornado.httpclient import AsyncHTTPClient
from tornadotest.handles.BaseHandle import MainHandler


class BlockHandler(MainHandler):

    async def post(self):
        client = AsyncHTTPClient()
        response = await client.fetch("http://www.mockbin.com/har")
        NbLog().info(json.loads(response.body))
        self.finish(response.body)
