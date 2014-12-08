"""
File: base.py
Base Tornado Handlers for BD TYPES.
(c) Vladyslav Ishchenko 12.2014, http://python-django.net
"""

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    """Base handler for MySQL.
    """
    @property
    def db(self):
        """Client for DB MySQL."""
        return self.application.db

    def get_current_user(self):
        """Overaided method, for getting User.
        User id saves in cookie.
        """
        user_id = self.get_secure_cookie("blogdemo_user")
        if not user_id: return None
        user = self.db.get("SELECT * FROM authors WHERE id = %s", int(user_id))
        return user


class BaseRiakHandler(RequestHandler):
    """Base handler for Riak.
    """
    @property
    def db(self):
        """Client for DB Riak."""
        return self.application.db

    def get_current_user(self):
        """Overaided method, for getting User.
        User id saves in cookie.
        """
        user_id = self.get_secure_cookie("blogdemo_user")
        if not user_id: return None
        user = self.db.bucket('authors').get(str(user_id))
        if not user.exists: return None
        return user.data

# TODO: Design of DB classes, one global for choosing BD TYPE.
# Need better ORM.
