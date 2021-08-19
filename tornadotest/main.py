import tornado.web
import tornado.ioloop
from handles.demoHandle import DemoHandler
from handles.blockHandle import BlockHandler


app = tornado.web.Application([
    (r"^/login/", DemoHandler),
    (r"^/block/", BlockHandler),
])

app.listen(9999)

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().start()
