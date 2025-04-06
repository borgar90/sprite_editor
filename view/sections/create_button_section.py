"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines CreateButtonSection, a reusable section that renders a large
"Create New Project" button at the bottom of the screen.
"""

import tkinter as tk
from view.sections.base_section import BaseSection


class CreateButtonSection(BaseSection):
    """
    Section that renders a centered "Create New Project" button.
    """

    def __init__(self, name, on_create):
        """
        Initialize the section.

        :param name: Identifier name
        :param on_create: Callback function to invoke when button is pressed
        """
        super().__init__(name)
        self.on_create = on_create

    def render(self, parent, **options):
        self.frame = tk.Frame(parent, bg="black")
        self.frame.pack(**options, fill="x", pady=(0, 30))

        button = tk.Button(
            self.frame,
            text="Create New Project",
            font=("Arial", 14),
            bg="#00bcd4",
            fg="white",
            relief="raised",
            height=2,
            width=25,
            command=self.on_create
        )
        button.pack()
