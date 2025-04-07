"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines ProjectModel which manages high-level project information
such as project name, save path, metadata, and version.
"""

import os
import json

class ProjectModel:
    """
    Handles project metadata and file/folder management.
    """

    def __init__(self, root_model):
        self.root = root_model
        self.name = "Untitled"
        self.version = "1.0"
        self.project_path = None
        self.metadata = {}  # Initialize metadata as an empty dictionary

    def load_projects(self, file_path):
        """
        Load project data from a JSON file.

        :param file_path: Path to the JSON file containing project data.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        with open(file_path, 'r') as file:
            self.metadata = json.load(file)

        print(f"Loaded projects from {file_path}")