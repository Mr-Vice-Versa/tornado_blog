"""
Templatetags, helper for rendering templates.
(c) Vladyslav Ishchenko 12.2014
"""

from tornado.web import UIModule


class EntryModule(UIModule):
    """Render ech item of entry model."""
    def render(self, entry):
        return self.render_string("modules/entry.html", entry=entry)
