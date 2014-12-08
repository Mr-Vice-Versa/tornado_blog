#!/home/vice-versa/vice-versa__Inspiron-N5110VV__01.12.2014/Development/Projects/tornado_blog/env_tornado_blog/bin/python
# ENV


"""
File: app.py
Tornado Blog app.
(c) Vladyslav Ishchenko 12.2014, http://python-django.net
"""

import torndb

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options
from tornado.web import Application

import riak

from settings import settings, DB_BACKEND_TYPE
from urls import url_patterns as handlers


class TornadoBlogApp(Application):
    """
    Tornado Blog Application
    DB: MySQL or Riak
    """
    def __init__(self):
        Application.__init__(self, handlers=handlers, **settings)

        if settings['db'] == DB_BACKEND_TYPE[1]:
            # MySQL global connection to the blog DB across all handlers.
            self.db = torndb.Connection(
                host=options.mysql_host, database=options.mysql_database,
                user=options.mysql_user, password=options.mysql_password)

        elif settings['db'] == DB_BACKEND_TYPE[0]:
            # Riak connection to the blog DB across all handlers.
            self.db = riak.RiakClient(
                protocol=options.riak_protocol, host=options.riak_host,
                http_port=options.riak_http_port)


def main():
    # HTTPServer initialization patterns listen: simple single-process
    options.parse_command_line()
    http_server = HTTPServer(TornadoBlogApp())
    http_server.listen(options.port)
    IOLoop.instance().start()


if __name__ == "__main__":
    print("HTTPServer start")
    main()
