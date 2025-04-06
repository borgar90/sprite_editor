"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines FileModel, which manages open .stj files, tab states, and unsaved changes.
"""

import os
import json

class FileModel:
    """
    Manages file data and tab state for open STJ files.
    Tracks file changes, save paths, and dirty flags.
    """

    def __init__(self, root_model):
        self.root = root_model
        self.open_files = []  # List of dicts: {"path": str, "dirty": bool}
        self.active_index = None

    def open(self, path):
        """
        Open a new file and add it to the tab system.
        """
        if os.path.isfile(path):
            self.open_files.append({"path": path, "dirty": False})
            self.active_index = len(self.open_files) - 1

    def mark_dirty(self, index):
        """
        Mark a file as changed.
        """
        if 0 <= index < len(self.open_files):
            self.open_files[index]["dirty"] = True

    def save(self, index):
        """
        Save a file to disk. Placeholder logic here.
        """
        if 0 <= index < len(self.open_files):
            # Simulate saving
            print(f"[FileModel] Saving {self.open_files[index]['path']}")
            self.open_files[index]["dirty"] = False

    def serialize(self):
        return {
            "open_files": self.open_files.copy(),
            "active_index": self.active_index
        }

    def load(self, data):
        self.open_files = data.get("open_files", [])
        self.active_index = data.get("active_index", None)

    def is_corrupt(self):
        return any(not os.path.exists(f["path"]) for f in self.open_files)
