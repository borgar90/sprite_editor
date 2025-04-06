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
from view.layouts.project_manager_layout import ProjectManagerLayout


class ProjectScreen(BaseScreen, tk.Frame):
    """
    Project selection screen that allows the user to select or create a project.
    It now uses a frame to be a valid Tkinter widget.
    """

    def __init__(self, app_context, master=None):
        """
        Initialize the project screen with app context and Tkinter master.

        :param app_context: Application context holding the shared state
        :param master: The Tkinter parent widget (usually the root or main window)
        """
        super().__init__(app_context)
        tk.Frame.__init__(self, master)  # Initialize as a Tkinter Frame
        self.master = master
        self.app_context = app_context
        self.layout = None
        self.find_project = self._find_project
        self.create_project = self._create_project
        self.select_project = self._select_project
        self.render()

    def render(self):
        """
        Render the project selection UI layout.
        """
        # Layout that will hold the project list and the button sections
        self.layout = ProjectManagerLayout(self)

        # Render the layout (which handles sections like project list, buttons, etc.)
        self.layout.render()

        self.pack(fill="both", expand=True)  # Ensure this frame fills its parent




    def _select_project(self, project_data):
        """
        Callback for when a project is selected from the list.
        """
        self.app_context.selected_project = project_data



    def _create_project(self):
        self.app_context.controller.project.create_new_project()


    def _find_project(self, project_data):
        project = self.app_context.selected_project
        if project is None:
            print(f"Project {project_data} not found.")
            return

        self.app_context.selected_project = project