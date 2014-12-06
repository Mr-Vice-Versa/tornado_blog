"""

"""

import json

from tornado.escape import json_encode
from tornado.web import HTTPError

from base import BaseHandler
from utils import DateTimeEncoder


class EntryMySQLAPIHandler(BaseHandler):
    """API handler for Entry object/objects.
    DB: MySQL
    """

    def _get_entry_or_404(self, entry_id):
        entry_queryset = self.db.get("SELECT * FROM entries WHERE id = %s", entry_id)
        if not entry_queryset: raise HTTPError(404)
        return entry_queryset

    # def writre_json_response(self, entry_queryset):
    #     """Dump to JSON and return write (response)."""
    #     response = json.dumps(entry_queryset, cls=DateTimeEncoder)
    #     self.set_header('Content-Type', 'application/javascript')
    #     self.write(json_encode(response))

    def get(self, *args, **kwargs):
        """Request GET."""
        if args:
            # Single entry object.
            entry_queryset  = self._get_entry_or_404(args[0])
        else:
            # List of entries.
            entry_queryset  = self.db.query("SELECT * FROM entries ORDER BY published " "DESC")
        response = json.dumps(entry_queryset, cls=DateTimeEncoder)
        self.set_header('Content-Type', 'application/javascript')
        # self.write(json_encode(response))
        self.write(response)

    def post(self, *args, **kwargs):
        """Request POST.
        Returns new entry or updated entry or HTTP code 400.
        """
        if args:
            entry_id = args[0]
            entry_queryset = self.db.get("SELECT * FROM entries WHERE id = %s", entry_id)
            if entry_queryset:
                # Update entry.
                self.put(entry_id)
            else:
                # Create new entry.
                self.create(entry_id, **kwargs)
        elif not args and not kwargs:
            # Bad request HTTP 400
            self.set_header('Content-Type', 'application/javascript')
            self.set_status(400)

    def put(self, *args, **kwargs):
        """Request PUT.
        Returns updated entry.
        """
        entry_queryset  = self._get_entry_or_404(args[0])
        self.set_header('Content-Type', 'application/javascript')
        # self.set_status(200)

    def create(self, *args, **kwargs):
        """Create new entry. Return HTTP 201 Created."""
        self.set_status(201)
        # insert to db new_entry
        # response = json.dumps(new_entry, cls=DateTimeEncoder)
        # self.set_header('Content-Type', 'application/javascript')
        # self.write(json_encode(response))
