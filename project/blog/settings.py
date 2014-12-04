"""
settings.py is python module for tornado app.
(c) Vladyslav Ishchenko 12.2014
"""

import os
from tornado.options import define

from uimodules import EntryModule


# Global settings for app.
DEBUG = True
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static/assets")
# Secure
XSRF_COOKIES = True
COOKIE_SECRET = "1234567890zxcvbnm"
# Auth
LOGIN_URL = "/auth/login"
# Blog settings
BLOG_TITLE = u"Tornado Blog"
BLOG_BACKGROUND_IMAGE = "img/home-bg.jpg"

# Make settings dict.
settings = dict(
    template_path=TEMPLATE_PATH,
    static_path=STATIC_PATH,
    xsrf_cookies=XSRF_COOKIES,
    cookie_secret=COOKIE_SECRET,
    login_url=LOGIN_URL,
    # UImodules
    ui_modules={"Entry": EntryModule},
    blog_title=BLOG_TITLE,
    blog_background_image=BLOG_BACKGROUND_IMAGE,
    # Debug
    debug=DEBUG,
)

# options setting.
define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_database", default="blog", help="blog database name")
define("mysql_user", default="blog", help="blog database user")
define("mysql_password", default="blog", help="blog database password")
