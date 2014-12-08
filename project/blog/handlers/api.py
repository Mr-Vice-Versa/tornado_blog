"""
File: api.py
Tornado Handlers for API.
(c) Vladyslav Ishchenko 12.2014, http://python-django.net

TODO: REFACTORING
TODO: ORM methods
TODO: ORM methods
TODO: Design, generalization, decomposition API
    DB design unique ID, Counters.
TODO: Compound data
TODO: Remove DYR!
TODO: Riak MapReduce, Riak ORM.
"""

import re
import json
import markdown
import unicodedata
import datetime

from tornado.web import authenticated
from tornado.web import HTTPError

from base import BaseHandler, BaseRiakHandler
from utils import DateTimeEncoder


class EntryMySQLAPIHandler(BaseHandler):
    """API handler for Entry object/objects.
    DB: MySQL
    """
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
        TODO: Update data.
        """
        json_data = self.decode(self.request.body)

        id = json_data.get("id", None)
        title = json_data.get("title", None)
        text = json_data.get("markdown")
        html = markdown.markdown(text)

        if id:
            pass
            # TODO: UPDATE
            # entry = self.db.get("SELECT * FROM entries WHERE id = %s", int(id))
            # if not entry: raise HTTPError(404)
            # slug = entry.slug
            # self.db.execute(
            #     "UPDATE entries SET title = %s, markdown = %s, html = %s "
            #     "WHERE id = %s", title, text, html, int(id))
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


class EntryRiakAPIHandler(BaseRiakHandler):
    """API handler for Entry object/objects.
    DB: Riak
    """
    def decode(self, data):
        return json.loads(data)

    def get(self, *args, **kwargs):
        """Request GET."""
        # TODO: Can be better.
        if args:
            # Single entry object.
            entry_queryset = self.db.bucket('entries').get(str(args[0]))
            if not entry_queryset.exists: raise HTTPError(404)
            # add entry.get_url for templates.
            entry_queryset.data['get_url'] = self.reverse_url("entry_id", entry_queryset.key)
            links = entry_queryset.links
            if links:
                bucket = str(links[0][0])
                key = str(links[0][1])
                if self.db.bucket(bucket).get(key).exists:
                    entry_queryset.data['author_name'] = self.db.bucket(bucket).get(key).data.get('name')
            entry_queryset = entry_queryset.data
        else:
            # List of entries.
            per_page = self.get_argument("per_page", None)
            if per_page:
                query = self.db.add('entries')
                query.map("function(v) { var data = JSON.parse(v.values[0].data); if(data) { return [[v.key, data]]; } return []; }")
                query.reduce_limit(int(per_page))
                entry_queryset = query.run()
            else:
                query = self.db.add('entries')
                query.map("function(v) { var data = JSON.parse(v.values[0].data); if(data) { return [[v.key, data]]; } return []; }")
                entry_queryset = query.run()
            # add entry.get_url for templates.
            for elem in entry_queryset:
                elem[1]['get_url'] = self.reverse_url("entry_id", elem[0])
            entry_queryset = [i[1]for i in entry_queryset]

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
            pass
            # TODO: UPDATE
            # entry = self.db.get("SELECT * FROM entries WHERE id = %s", int(id))
            # if not entry: raise HTTPError(404)
            # slug = entry.slug
            # self.db.execute(
            #     "UPDATE entries SET title = %s, markdown = %s, html = %s "
            #     "WHERE id = %s", title, text, html, int(id))
        else:
            slug = unicodedata.normalize("NFKD", title).encode(
                "ascii", "ignore")
            slug = re.sub(r"[^\w]+", " ", slug)
            slug = "-".join(slug.lower().strip().split())
            entries = self.db.bucket('entries')
            if not slug: slug = "entry"
            entries_slugs = [entries.get(entry_key).data.get('slug', None) for entry_key in entries.get_keys()]
            while True:
                # TODO: Bad BigO
                if slug not in entries_slugs:
                    break
                slug += "-2"
            current_user_id = str(self.current_user.get('id'))
            now = json.dumps(datetime.datetime.now(), cls=DateTimeEncoder)
            data={
                'author_id': current_user_id,
                'title': title,
                'slug': slug,
                'text': text,
                'html': html,
                'published': now,
                'updated': now
                }
            entry = entries.new(data=data, content_type='application/json')
            entry.store()
            author = self.db.bucket('authors').get(current_user_id, None)
            if author:
                author.add_link(entry)
                author.store()
                entry.add_link(author)
                entry.store()

        self.set_header('Content-Type', 'application/javascript')
        self.set_status(201)
        self.write(json.dumps(entry.data, cls=DateTimeEncoder))
