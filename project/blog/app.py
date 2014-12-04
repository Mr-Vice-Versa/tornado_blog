#!/home/vice-versa/vice-versa__Inspiron-N5110VV__01.12.2014/Development/Projects/tornado_blog/env_tornado_blog/bin/python
# Your env here.

"""
Tornado Blog app.
(c) Vladyslav Ishchenko 12.2014
"""

import torndb

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options
from tornado.web import Application

from settings import settings
from urls import url_patterns as handlers


class TornadoBlogApp(Application):
    """

    """
    def __init__(self):
        Application.__init__(self, handlers=handlers, **settings)
        # One global connection to the blog DB across all handlers.
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)


def main():
    # HTTPServer initialization patterns listen: simple single-process
    options.parse_command_line()
    http_server = HTTPServer(TornadoBlogApp())
    http_server.listen(options.port)
    IOLoop.instance().start()


if __name__ == "__main__":
    print("HTTPServer start")
    main()
