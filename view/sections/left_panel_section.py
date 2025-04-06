"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines the LeftPanelSection class, which represents the left panel of the default screen.
It typically contains tools or navigation related to the current mode.
"""

import tkinter as tk
from view.sections.base_section import BaseSection


class LeftPanelSection(BaseSection):
    """
    GUI section placed on the left side of the screen, usually containing tool buttons or navigation.
    """

    def render(self, parent, **options):
        """
        Render the section inside a new frame, positioned using grid.

        :param parent: The parent widget (usually root or layout container)
        :param options: Options passed to the .grid() method
        """
        self.frame = tk.Frame(parent, bg="#2b2b2b", width=200)
        self.frame.grid(**options)
        self.frame.grid_propagate(False)

        # Placeholder content for now
        label = tk.Label(self.frame, text="Left Panel", fg="white", bg="#2b2b2b")
        label.pack(padx=10, pady=10)
