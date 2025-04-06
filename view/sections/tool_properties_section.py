"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This section defines ToolPropertiesSection, a dynamic right-side panel
that displays UI inputs depending on the selected tool and canvas element.
"""

import tkinter as tk
from view.sections.base_section import BaseSection


class ToolPropertiesSection(BaseSection):
    """
    Panel on the right side of the screen.
    Dynamically changes its content based on the selected tool and grid item.
    """

    def render(self, parent, **options):
        self.frame = tk.Frame(parent, bg="#202020", width=280)
        self.frame.grid(**options)
        self.frame.grid_propagate(False)

        self.header = tk.Label(
            self.frame,
            text="Tool Properties",
            bg="#202020",
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.header.pack(pady=(10, 5))

        self.content = tk.Frame(self.frame, bg="#2a2a2a")
        self.content.pack(fill="both", expand=True, padx=10, pady=5)

        # Placeholder input (to be dynamically replaced)
        placeholder = tk.Label(self.content, text="No tool selected", bg="#2a2a2a", fg="white")
        placeholder.pack(pady=20)

    def update_content(self, widgets):
        """
        Replace current inputs with a new list of widgets.

        :param widgets: List of Tk widgets to pack
        """
        for child in self.content.winfo_children():
            child.destroy()
        for widget in widgets:
            widget.pack(pady=5, anchor="w")
