"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 2.0.0

This module defines the ProjectScreen class using the new reusable layout/section/element architecture.
It composes a vertical layout with a top logo, scrollable project list section, and a create button section.
"""

import os
import tkinter as tk
from view.screens.base_screen import BaseScreen
from view.layouts.vertical_scroll_layout import VerticalScrollLayout
from view.sections.project_list_section import ProjectListSection
from view.sections.create_button_section import CreateButtonSection


class ProjectScreen(BaseScreen):
    """
    Project selection screen composed from reusable sections and layout.
    """

    def __init__(self, app_context):
        super().__init__(app_context)
        self.project_data = []

    def render(self, root):
        self._load_projects()
        self.layout = VerticalScrollLayout(root)

        # Logo (not a section, placed inline)
        logo = tk.Label(root, text="SpriteToJSON", font=("Arial", 32), fg="white", bg="black")
        logo.pack(pady=(30, 10))

        list_section = ProjectListSection(
            name="ProjectList",
            project_data=self.project_data,
            on_select=self._select_project,
            on_find=self._find_project
        )

        create_section = CreateButtonSection(
            name="CreateButton",
            on_create=self._create_project
        )

        self.layout.add_section(list_section)
        self.layout.add_section(create_section)
        self.layout.render()

    def _load_projects(self):
        """
        Load all available projects from /projects with preview.png.
        """
        folder = "projects"
        if not os.path.exists(folder):
            return

        for name in os.listdir(folder):
            path = os.path.join(folder, name)
            if os.path.isdir(path):
                preview = os.path.join(path, "preview.png")
                if os.path.exists(preview):
                    self.project_data.append({
                        "title": name,
                        "img_path": preview,
                        "path": path
                    })

    def _select_project(self, project_data):
        """
        Callback for when a project is selected from the list.
        """
        self.app_context.selected_project = project_data

    def _find_project(self):
        print("[ProjectScreen] Find project clicked")

    def _create_project(self):
        self.app_context.controller.project.create_new_project()
