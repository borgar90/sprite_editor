"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines the RightPanelSection class, which represents the right panel of the default screen.
Typically used to show configuration options, properties, or contextual tools.
"""

import tkinter as tk
from view.sections.base_section import BaseSection


class RightPanelSection(BaseSection):
    """
    GUI section placed on the right side of the screen.
    Typically used for property panels, settings, or context-aware tools.
    """

    def render(self, parent, **options):
        """
        Render the section inside a fixed-width frame, positioned using grid.

        :param parent: The parent widget (usually root or layout container)
        :param options: Options passed to the .grid() method
        """
        self.frame = tk.Frame(parent, bg="#2b2b2b", width=250)
        self.frame.grid(**options)
        self.frame.grid_propagate(False)

        # Placeholder content for now
        label = tk.Label(self.frame, text="Right Panel", fg="white", bg="#2b2b2b")
        label.pack(padx=10, pady=10)
