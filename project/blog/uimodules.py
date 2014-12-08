"""
Files: uimodules.py
Templatetags or helper for rendering data into templates.
(c) Vladyslav Ishchenko 12.2014, http://python-django.net
"""

from tornado.web import UIModule


class EntryModule(UIModule):
    """Render entry model."""
    def render(self, entry):
        return self.render_string("modules/entry.html", entry=entry)
