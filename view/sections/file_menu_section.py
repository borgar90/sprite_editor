"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This section defines the FileMenuSection, the topmost menu bar in the application.
It provides file-related commands such as New, Open, Save, and Exit.
"""

import tkinter as tk
from tkinter import Menu
from view.sections.base_section import BaseSection


class FileMenuSection(BaseSection):
    """
    Top-level file menu section rendered using a native Tkinter menu.
    Attached directly to the root window.
    """

    def render(self, parent, **options):
        self.frame = tk.Frame(parent)
        self.frame.grid(**options)

        menubar = Menu(parent)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="New Project", command=self.new_project)
        file_menu.add_command(label="Open Project", command=self.open_project)
        file_menu.add_command(label="Save", command=self.save)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=parent.quit)

        menubar.add_cascade(label="File", menu=file_menu)
        parent.master.config(menu=menubar)

    def new_project(self):
        print("[FileMenu] New Project")

    def open_project(self):
        print("[FileMenu] Open Project")

    def save(self):
        print("[FileMenu] Save")
