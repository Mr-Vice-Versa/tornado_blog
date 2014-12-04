"""
(c) Vladyslav Ishchenko 12.2014
"""

from tornado.web import asynchronous

from base import BaseHandler


class IndexHandler(BaseHandler):
    """Index page of Blog."""
    template = "base.html"

    @asynchronous
    def get(self):
        # Entries queryset.
        queryset = self.db.query("SELECT * FROM entries ORDER BY published "
                                "DESC LIMIT 5")
        #
        if not queryset:
            self.redirect("/compose")
            return
        # Render template.
        self.render(self.template, entries=queryset)
