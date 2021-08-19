import json
import sys

sys.path.append('C:\\PycharmProjects\\autoTest')

from tornadotest.intergration.logWriter import NbLog
from tornado.httpclient import AsyncHTTPClient
from tornadotest.handles.BaseHandle import MainHandler


class DemoHandler(MainHandler):

    async def post(self):
        request_body = json.loads(self.request.body)
        log = NbLog(task_name=request_body['taskNo'], file_name=request_body['taskNo'])
        log.info(request_body)
        client = AsyncHTTPClient()
        response = await client.fetch("http://www.mockbin.com/har")
        log.info(json.loads(response.body))
        self.finish(response.body)


