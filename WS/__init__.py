# __init__.py
import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")

class userRequestHandler(tornado.web.RequestHandler):
    def get(self):
        id=int(self.get_argument("id"))
        self.write(str(id))
    def post(self):
        id=int(self.get_argument("id"))
        self.write(str(id))

def main():
    """Construct and serve the tornado application."""
    app = tornado.web.Application([
        ('/', basicRequestHandler),
        ('/user', userRequestHandler)
    ])
    app.listen(8881)
    print("Listening on port 8881")
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
