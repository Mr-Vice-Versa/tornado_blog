"""
(c) Vladyslav Ishchenko 12.2014
"""

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    """
    """
    @property
    def db(self):
        """
        """
        return self.application.db

    def get_current_user(self):
        """
        """
        user_id = self.get_secure_cookie("blogdemo_user")
        if not user_id: return None
        user = self.db.get("SELECT * FROM authors WHERE id = %s", int(user_id))
        return user
