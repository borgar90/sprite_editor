# view/layouts/layout.py
import tkinter as tk
from view.sections.section import Section

class Layout:
    def __init__(self, parent: tk.Widget):
        self.parent = parent
        self.sections = []

    def add_section(self, section: Section, **pack_options):
        """Legg til en seksjon og pakk den inn i layouten med valgte opsjoner."""
        self.sections.append(section)
        section.render(**pack_options)

    def clear(self):
        """Fjerner alle widgets i layouten."""
        for section in self.sections:
            section.destroy()
        self.sections.clear()
