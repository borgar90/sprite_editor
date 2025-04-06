"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines the MainCanvasSection class, which represents the center canvas area.
It is intended to host the scrollable, zoomable drawing or sprite editing surface.
"""

import tkinter as tk
from view.sections.base_section import BaseSection


class MainCanvasSection(BaseSection):
    """
    Central section that holds the main drawing canvas and its scrollbars.
    """

    def render(self, parent, **options):
        """
        Render the canvas section in the center of the window.

        :param parent: The parent widget (typically the root container)
        :param options: Options passed to .grid()
        """
        self.frame = tk.Frame(parent, bg="#1e1e1e")
        self.frame.grid(**options)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Create a canvas with scrollbars
        canvas = tk.Canvas(self.frame, bg="#1e1e1e", highlightthickness=0)
        canvas.grid(row=0, column=0, sticky="nsew")

        x_scroll = tk.Scrollbar(self.frame, orient="horizontal", command=canvas.xview)
        x_scroll.grid(row=1, column=0, sticky="ew")

        y_scroll = tk.Scrollbar(self.frame, orient="vertical", command=canvas.yview)
        y_scroll.grid(row=0, column=1, sticky="ns")

        canvas.configure(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

        self.canvas = canvas  # Optional reference if needed later
