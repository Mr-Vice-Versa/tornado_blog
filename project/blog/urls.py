"""
(c) Vladyslav Ishchenko 12.2014
"""

from tornado.web import url

from handlers.blog import IndexHandler
from handlers.api import EntryMySQLAPIHandler
from handlers.auth import AuthLoginHandler, AuthLogoutHandler


# Site
url_site_patterns = [
    url(r"/", IndexHandler, name="index"),
    url(r"/auth/login", AuthLoginHandler),
    url(r"/auth/logout", AuthLogoutHandler),
]

# API
url_api_patterns = [
    url(r"/entry$", EntryMySQLAPIHandler, name="entry_list"),
    url(r"/entry/(\d+)$", EntryMySQLAPIHandler, name="entry_id"),
    # url(r"/archive", ArchiveHandler),

]

url_patterns = url_site_patterns + url_api_patterns
