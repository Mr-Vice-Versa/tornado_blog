"""
File: utils.py
Utils classes.
(c) Vladyslav Ishchenko 12.2014, http://python-django.net
"""

import datetime
import json


class DateTimeEncoder(json.JSONEncoder):
    """For daetime dumps."""
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()
        else:
            return super(DateTimeEncoder, self).default(obj)
