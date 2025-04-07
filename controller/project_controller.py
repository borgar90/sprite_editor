"""
Author: Borgar Flaen Stensrud
Date: 2025-04-07
Version: 1.0.0

This module defines ProjectController, which manages project creation and loading.
"""

import os
import json

class ProjectController:
    """
    Manages project creation and loading.
    """

    def __init__(self):
        self.project_path = None
        self.project_name = None
        self.media_folder = None
        self.maps_folder = None
        self.config_folder = None

    def create_new_project(self, directory, name):
        """Creates a new project with the specified directory and name."""
        self.project_path = os.path.join(directory, name)
        self.project_name = name

        os.makedirs(self.project_path, exist_ok=True)
        self.media_folder = os.path.join(self.project_path, "images")
        self.maps_folder = os.path.join(self.project_path, "maps")
        self.config_folder = os.path.join(self.project_path, "config")

        for folder in [self.media_folder, self.maps_folder, self.config_folder]:
            os.makedirs(folder, exist_ok=True)

        with open(os.path.join(self.project_path, f"{name}.stjproj"), "w") as f:
            json.dump({"name": name}, f)
        
        self.app_context.app_state.set_state("default")

    def load_project(self, proj_file_path):
        """Loads an existing project from the specified file path."""
        with open(proj_file_path) as f:
            data = json.load(f)
            self.project_path = os.path.dirname(proj_file_path)
            self.project_name = data["name"]
            self.media_folder = os.path.join(self.project_path, "images")
            self.maps_folder = os.path.join(self.project_path, "maps")
            self.config_folder = os.path.join(self.project_path, "config")