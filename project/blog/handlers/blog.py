"""
(c) Vladyslav Ishchenko 12.2014
"""

from base import BaseHandler, BaseRiakHandler


class IndexHandler(BaseHandler):
    """MySQL. Index page of Blog.
    Return 5 entries or redirect to create one.
    """
    template = "index.html"

    def get(self):
        # Entries queryset limited by 5 items.
        queryset = self.db.query("SELECT * FROM entries ORDER BY published " "DESC LIMIT 5")
        # add entry.get_url for templates.
        for elem in queryset:
            elem['get_url'] = self.reverse_url("entry_id", elem.id)
        # Render template.
        self.render(self.template, entries=queryset, handler=self)

    def get_author_name(self, author_id, field="*"):
        query = "SELECT {field} FROM authors WHERE id = {id}".format(field=field, id=author_id)
        queryset = self.db.query(query)
        return queryset[0] if field == "*" else queryset[0][field]


class IndexRiakHandler(BaseRiakHandler):
    """Riack. Index page of Blog.
    Return 5 entries or redirect to create one.
    """
    template = "index.html"

    def get(self):
        # Entries queryset limited by 5 items.
        # Map/Reduce
        query = self.db.add('entries')
        query.map("function(v) { var data = JSON.parse(v.values[0].data); if(data) { return [[v.key, data]]; } return []; }")
        query.reduce_limit(5)
        queryset = query.run()
        # add entry.get_url for templates.
        if queryset:
            for elem in queryset:
                elem[1]['get_url'] = self.reverse_url("entry_id", elem[0])
        queryset =[i[1]for i in queryset]
        # Render template.
        self.render(self.template, entries=queryset, handler=self)

    def get_author_name(self, author_id, field="*"):
        author = self.db.bucket('authors').get(str(author_id)).exists
        if not author.exists:
            return
        else:
            return author.data if field == "*" else author.data[field]
