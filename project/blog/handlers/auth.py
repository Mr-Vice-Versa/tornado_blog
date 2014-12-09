"""
File: auth.py
Login via GoogleMixin

Tornado do not set csrf_token sometimes,
but when call self.csrf_token it all will be alright.
"""

from tornado.web import asynchronous
from tornado.auth import GoogleMixin

from base import BaseHandler, BaseRiakHandler


class AuthLoginHandler(BaseHandler, GoogleMixin):
    @asynchronous
    def get(self):
        if self.get_argument("openid.mode", None):
            self.get_authenticated_user(self._on_auth)
            return
        self.authenticate_redirect()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Google auth failed")
        author = self.db.get("SELECT * FROM authors WHERE email = %s",
                             user["email"])
        if not author:
            # Auto-create first author
            any_author = self.db.get("SELECT * FROM authors LIMIT 1")
            if not any_author:
                author_id = self.db.execute(
                    "INSERT INTO authors (email,name) VALUES (%s,%s)",
                    user["email"], user["name"])
            else:
                self.redirect("/")
                return
        else:
            author_id = author["id"]
        self.set_secure_cookie("blogdemo_user", str(author_id))
        self.redirect(self.get_argument("next", "/"))


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("blogdemo_user")
        self.redirect(self.get_argument("next", "/"))


class AuthLoginRiakHandler(BaseRiakHandler, GoogleMixin):
    @asynchronous
    def get(self):
        if self.get_argument("openid.mode", None):
            self.get_authenticated_user(self._on_auth)
            return
        self.authenticate_redirect()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Google auth failed")

        authors = self.db.bucket('authors')
        author_exsists = False
        for author_key in authors.get_keys():
            author_dict_values = authors.get(author_key).data
            if author_dict_values.get('email', None) == user["email"]:
                author = authors.get(str(author_key))
                author_exsists = True
                break
        if not author_exsists:
            # Auto-create first author
            any_author = authors.get_keys()[0] if authors.get_keys() else None
            if not any_author:
                author2 = authors.new(data={'email': user["email"], 'name': user["name"],},
                                      content_type='application/json')
                author2.store()
                author_id = author2.key
                author2.data['id'] = author2.key
                author2.store()
            else:
                self.redirect("/")
                return
        else:
            author_id = author.key
        self.set_secure_cookie("blogdemo_user", str(author_id))
        self.redirect(self.get_argument("next", "/"))


class AuthLogoutRiakHandler(BaseRiakHandler):
    def get(self):
        self.clear_cookie("blogdemo_user")
        self.redirect(self.get_argument("next", "/"))
