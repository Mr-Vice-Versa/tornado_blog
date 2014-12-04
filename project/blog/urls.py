"""
(c) Vladyslav Ishchenko 12.2014
"""

from tornado.web import url

from handlers.blog import IndexHandler


# Site
url_site_patterns = [
    url(r"/", IndexHandler, name="index"),
]

# API
url_api_patterns = []

url_patterns = url_site_patterns + url_api_patterns
