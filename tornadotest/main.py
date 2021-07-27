import tornado.web
import tornado.ioloop
import json, time
from intergration.logHandle import NbLog
from tornado.httpclient import AsyncHTTPClient
from handles.demo_handle import Handler
from handles.block_handle import BlockHandler


app = tornado.web.Application([
    (r"^/login/", Handler),
    (r"^/block/", BlockHandler),
])

app.listen(9999)

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().start()
