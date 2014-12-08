"""
File: settings.py
Settings python module for tornado app.
(c) Vladyslav Ishchenko 12.2014, http://python-django.net
"""

import os
from tornado.options import define

from uimodules import EntryModule


# Global settings for app.
DEBUG = True
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static/assets")
# Secure
XSRF_COOKIES = False
COOKIE_SECRET = "123554567890zxcvbnm1111"
# Auth
LOGIN_URL = "/auth/login"
# Blog settings
BLOG_TITLE = u"Tornado Blog"
BLOG_BACKGROUND_IMAGE = "img/home-bg.jpg"
# List of poseble database types
DB_BACKEND_TYPE = ['riak', 'mysql']
# Use Database
DB = DB_BACKEND_TYPE[0]


# Tornado server
define("port", default=8888, help="run on the given port", type=int)

if DB == DB_BACKEND_TYPE[1]:
    # MySql, options setting.
    define("mysql_host", default="127.0.0.1:3306", help="blog database host")
    define("mysql_database", default="blog", help="blog database name")
    define("mysql_user", default="blog", help="blog database user")
    define("mysql_password", default="blog", help="blog database password")

elif DB == DB_BACKEND_TYPE[0]:
    # Riak, options setting.
    define("riak_host", default="127.0.0.1", help="riak host")
    define("riak_http_port", default="8098", help="riak http_port")
    define("riak_protocol", default="http", help="riak protocol")


# Make settings dict.
settings = dict(
    template_path=TEMPLATE_PATH,
    static_path=STATIC_PATH,
    xsrf_cookies=XSRF_COOKIES,
    cookie_secret=COOKIE_SECRET,
    login_url=LOGIN_URL,
    ui_modules={"Entry": EntryModule},
    blog_title=BLOG_TITLE,
    blog_background_image=BLOG_BACKGROUND_IMAGE,
    db=DB,
    debug=DEBUG,
)
