"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines VerticalScrollLayout, a layout that vertically stacks sections.
It is ideal for screens with scrollable middle content and fixed bottom areas.
"""

from view.layouts.base_layout import BaseLayout


class VerticalScrollLayout(BaseLayout):
    """
    A layout that stacks sections vertically in the given order.
    Useful for full-height flows such as project selection screens.
    """

    def render(self):
        """
        Render all sections using pack layout vertically.
        Each section defines its own padding and sizing.
        """
        for section, _ in self.sections:
            section.render(self.root)
