"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This section defines ProjectBarSection, which appears below the file menu.
It shows the active project name, current open files, or navigation tabs.
"""

import tkinter as tk
from view.sections.base_section import BaseSection


class ProjectBarSection(BaseSection):
    """
    Displays the current project title and potentially open files or file tabs.
    Lives directly under the FileMenuSection.
    """

    def render(self, parent, **options):
        self.frame = tk.Frame(parent, bg="#292929", height=30)
        self.frame.grid(**options, sticky="ew")
        self.frame.grid_propagate(False)

        self.label = tk.Label(
            self.frame,
            text="Project: Untitled",
            bg="#292929",
            fg="white",
            font=("Arial", 10, "bold")
        )
        self.label.pack(side="left", padx=10, pady=5)

    def update_project_name(self, name):
        """
        Update the visible project name label.

        :param name: New project name to display
        """
        self.label.config(text=f"Project: {name}")