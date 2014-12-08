"""
File: urls.py
URL Routers for Tornado Handlers.
(c) Vladyslav Ishchenko 12.2014, http://python-django.net
TODO: Better design URL.
"""

from tornado.web import url

from settings import settings, DB_BACKEND_TYPE
from handlers.blog import IndexHandler, IndexRiakHandler
from handlers.api import EntryMySQLAPIHandler, EntryRiakAPIHandler
from handlers.auth import (AuthLoginHandler, AuthLogoutHandler,
                           AuthLoginRiakHandler, AuthLogoutRiakHandler)


# TODO: Select Tornado handler by DB TYPE.
if settings['db'] == DB_BACKEND_TYPE[1]:
    # MySql
    IndexHandler = IndexHandler
    AuthLoginHandler = AuthLoginHandler
    AuthLogoutHandler = AuthLogoutHandler
    EntryAPIHandler = EntryMySQLAPIHandler
    api_url = r"/entry/(\d+)$"
elif settings['db'] == DB_BACKEND_TYPE[0]:
    # Riak
    api_url = r"/entry/([^/]+)"
    IndexHandler = IndexRiakHandler
    AuthLoginHandler = AuthLoginRiakHandler
    AuthLogoutHandler = AuthLogoutRiakHandler
    EntryAPIHandler = EntryRiakAPIHandler


# URL patterns for site.
url_site_patterns = [
    url(r"/", IndexHandler, name="index"),
    url(r"/auth/login", AuthLoginHandler),
    url(r"/auth/logout", AuthLogoutHandler)
]

# URL patterns for API.
url_api_patterns = [
    # TODO: ugly url
    url(api_url, EntryAPIHandler, name="entry_id"),
    url(r"/entry", EntryAPIHandler, name="entry_list")
]


# All URL patterns
url_patterns = url_site_patterns + url_api_patterns
