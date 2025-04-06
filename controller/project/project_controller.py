"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.2.0

ProjectController handles all project-related actions including creation,
loading metadata, and basic validation.
"""

import os
import tkinter as tk
from tkinter import simpledialog, filedialog


class ProjectController:
    """
    Handles high-level project structure and metadata control.
    Used after splash when transitioning into project selection or main editing.
    """

    def __init__(self, root_controller):
        self.root = root_controller
        self.model = root_controller.app_context.model.project
        self.view = root_controller.app_context.view  # for screen/view access

    def create_new_project(self, name=None, path=None):
        """
        Prompt for project name and folder path if not provided.
        Create directory and load project into workspace.
        """
        if not name:
            name = simpledialog.askstring("Project Name", "Enter new project name:")
            if not name:
                print("[ProjectController] No name entered, cancelled.")
                return

        if not path:
            chosen_folder = filedialog.askdirectory(title="Select or create folder for project")
            if not chosen_folder:
                print("[ProjectController] No folder selected, cancelled.")
                return
            path = os.path.join(chosen_folder, name)

        if not os.path.exists(path):
            os.makedirs(path)

        self.model.create(name, path)
        print(f"[ProjectController] Created new project: {name} at {path}")
        self.view.show_screen("CoreScreen")

    def load_project_from_data(self, data):
        self.model.load(data)
        print(f"[ProjectController] Loaded project: {self.model.name}")
        self.view.show_screen("CoreScreen")

    def get_current_project_name(self):
        return self.model.name

    def is_valid(self):
        return not self.model.is_corrupt()