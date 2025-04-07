"""
Author: Borgar Flaen Stensrud
Date: 2025-04-07
Version: 1.0.0

This module defines MenuBar, which provides the application's menu bar.
It includes file, project, edit, view, and help menus.
"""

import tkinter as tk
from tkinter import filedialog, messagebox

class MenuBar(BaseView):
    """
    Provides the application's menu bar.
    """

    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.menu = tk.Menu(self.root)

        self._build_file_menu()
        self._build_project_menu()
        self._build_edit_menu()
        self._build_view_menu()
        self._build_help_menu()

    def _build_file_menu(self):
        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Open Image...", command=self.controller.open_image)
        file_menu.add_command(label="Export JSON...", command=self.controller.export_json)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu.add_cascade(label="File", menu=file_menu)

    def _build_project_menu(self):
        project_menu = tk.Menu(self.menu, tearoff=0)
        project_menu.add_command(label="New Project", command=self.controller.new_project)
        project_menu.add_command(label="Open Project", command=self.controller.open_project)
        project_menu.add_command(label="Save Project", command=self.controller.save_project)
        project_menu.add_command(label="Close Project", command=self.controller.close_project)
        self.menu.add_cascade(label="Project", menu=project_menu)

    def _build_edit_menu(self):
        edit_menu = tk.Menu(self.menu, tearoff=0)
        edit_menu.add_command(label="Undo", state="disabled")
        edit_menu.add_command(label="Redo", state="disabled")
        self.menu.add_cascade(label="Edit", menu=edit_menu)

    def _build_view_menu(self):
        view_menu = tk.Menu(self.menu, tearoff=0)
        view_menu.add_command(label="Switch to Painter", command=lambda: self.controller.switch_screen("paint"))
        view_menu.add_command(label="Switch to Preview", command=lambda: self.controller.switch_screen("preview"))
        self.menu.add_cascade(label="View", menu=view_menu)

    def _build_help_menu(self):
        help_menu = tk.Menu(self.menu, tearoff=0)
        help_menu.add_command(label="About", command=self._show_about)
        self.menu.add_cascade(label="Help", menu=help_menu)

    def _show_about(self):
        messagebox.showinfo("About", "SpriteToJSON GUI\nCreated by Borgar Flaen Stensrud.")