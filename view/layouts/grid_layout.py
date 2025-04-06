"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines the GridLayout class, which arranges sections using Tkinter's grid geometry manager.
"""

from view.layouts.base_layout import BaseLayout


class GridLayout(BaseLayout):
    """
    A layout that arranges sections using Tkinter's grid manager.
    Suitable for placing elements in a row-column configuration.
    """

    def render(self):
        """
        Render all registered sections using grid placement.
        Expands the center column (typically canvas) by setting grid weights.
        """
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)  # Center column (canvas)

        for section, options in self.sections:
            section.render(self.root, **options)
