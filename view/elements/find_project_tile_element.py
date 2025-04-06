"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines FindProjectTileElement, a reusable GUI element for locating existing projects.
Displayed alongside other project tiles, it triggers a callback when clicked.
"""

import tkinter as tk
from view.elements.base_element import BaseElement


class FindProjectTileElement(BaseElement):
    """
    A clickable tile styled similarly to project tiles, used to find existing projects.
    """

    def __init__(self, master, on_click, **kwargs):
        """
        Initialize the find project tile.

        :param master: Parent container
        :param on_click: Callback when tile is clicked
        :param kwargs: Optional styling overrides
        """
        super().__init__(master, **kwargs)
        self.on_click = on_click

    def render(self, master=None):
        if master:
            self.master = master

        self.widget = tk.Frame(self.master, bg="#1e1e1e", bd=2, relief="solid", height=120)
        self.widget.pack(padx=20, pady=10, fill="x")

        label = tk.Label(
            self.widget,
            text="Find Existing Project",
            fg="white",
            bg="#1e1e1e",
            font=("Arial", 14)
        )
        label.pack(pady=40)

        for widget in (self.widget, label):
            widget.bind("<Button-1>", lambda e: self._on_click())

    def _on_click(self):
        if self.on_click:
            self.on_click()
