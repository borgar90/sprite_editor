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
        self.metadata = {}

    def create(self, name, path):
        """
        Create a new project.

        :param name: Project name
        :param path: Path to the project folder
        """
        self.name = name
        self.project_path = path
        self.metadata = {"created": True}
        os.makedirs(path, exist_ok=True)

    def serialize(self):
        """
        Return project state as a dictionary for snapshot or save.
        """
        return {
            "name": self.name,
            "version": self.version,
            "path": self.project_path,
            "metadata": self.metadata.copy()
        }

    def load(self, data):
        """
        Load project state from serialized dictionary.
        """
        self.name = data.get("name", "Untitled")
        self.version = data.get("version", "1.0")
        self.project_path = data.get("path", None)
        self.metadata = data.get("metadata", {})

    def is_corrupt(self):
        """
        Determine if project state is corrupted (e.g., missing path).
        """
        return not self.project_path or not os.path.isdir(self.project_path)