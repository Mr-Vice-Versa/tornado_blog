"""

"""

import re
import json
import markdown
import unicodedata

from tornado.web import authenticated
from tornado.escape import json_encode
from tornado.web import HTTPError

from base import BaseHandler
from utils import DateTimeEncoder


class EntryMySQLAPIHandler(BaseHandler):
    """API handler for Entry object/objects.
    DB: MySQL
    """

    def encode(self, data):
        return json.dumps(data)

    def decode(self, data):
        return json.loads(data)

    def get(self, *args, **kwargs):
        """Request GET."""
        if args:
            # Single entry object.
            entry_queryset = self.db.get("SELECT * FROM entries WHERE id = %s", args[0])
            if not entry_queryset: raise HTTPError(404)
            # add entry.get_url for templates.
            entry_queryset['get_url'] = self.reverse_url("entry_id", entry_queryset.id)
        else:
            # List of entries.
            per_page = self.get_argument("per_page", None)
            if per_page:
                sql = "SELECT * FROM entries ORDER BY published DESC LIMIT {0}".format(per_page)
            else:
                sql = "SELECT * FROM entries ORDER BY published DESC"
            entry_queryset  = self.db.query(sql)

            # entry_queryset  = self.db.query("SELECT * FROM entries ORDER BY published " "DESC")
            # add entry.get_url for templates.
            for elem in entry_queryset:
                elem['get_url'] = self.reverse_url("entry_id", elem.id)

        response = json.dumps(entry_queryset, cls=DateTimeEncoder)
        self.set_header('Content-Type', 'application/javascript')
        self.write(response)

    @authenticated
    def post(self, *args, **kwargs):
        """Request POST.
        Returns new entry or updated entry or HTTP code 400.
        """
        json_data = self.decode(self.request.body)

        id = json_data.get("id", None)
        title = json_data.get("title", None)
        text = json_data.get("markdown")
        html = markdown.markdown(text)

        if id:
            entry = self.db.get("SELECT * FROM entries WHERE id = %s", int(id))
            if not entry: raise HTTPError(404)
            slug = entry.slug
            self.db.execute(
                "UPDATE entries SET title = %s, markdown = %s, html = %s "
                "WHERE id = %s", title, text, html, int(id))
        else:
            slug = unicodedata.normalize("NFKD", title).encode(
                "ascii", "ignore")
            slug = re.sub(r"[^\w]+", " ", slug)
            slug = "-".join(slug.lower().strip().split())
            if not slug: slug = "entry"
            while True:
                e = self.db.get("SELECT * FROM entries WHERE slug = %s", slug)
                if not e: break
                slug += "-2"
            self.db.execute(
                "INSERT INTO entries (author_id,title,slug,markdown,html,"
                "published) VALUES (%s,%s,%s,%s,%s,UTC_TIMESTAMP())",
                self.current_user.id, title, slug, text, html)
            entry = self.db.get("SELECT * FROM entries WHERE slug = %s", slug)
        self.set_header('Content-Type', 'application/javascript')
        self.set_status(201)
        self.write(json.dumps(entry, cls=DateTimeEncoder))
