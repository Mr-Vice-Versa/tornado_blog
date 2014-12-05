"""
(c) Vladyslav Ishchenko 12.2014
"""

from base import BaseHandler


class IndexHandler(BaseHandler):
    """Index page of Blog.
    Return 5 entries or redirect to create one.
    """
    template = "index.html"

    def get(self):
        # Entries queryset limited by 5 items.
        queryset = self.db.query("SELECT * FROM entries ORDER BY published " "DESC LIMIT 5")
        if not queryset:
            self.redirect("/compose")
            return
        # Render template.
        self.render(self.template, entries=queryset, handler=self)

    def get_author_name(self, author_id, field="*"):
        query = "SELECT {field} FROM authors WHERE id = {id}".format(field=field, id=author_id)
        queryset = self.db.query(query)
        return queryset[0] if field == "*" else queryset[0][field]
