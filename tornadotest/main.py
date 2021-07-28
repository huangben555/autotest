import tornado.web
import tornado.ioloop
from handles.demo_handle import Handler
from handles.block_handle import BlockHandler


app = tornado.web.Application([
    (r"^/login/", Handler),
    (r"^/block/", BlockHandler),
])

app.listen(9999)

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().start()
