"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This controller defines FileController, which manages open .stj files,
tab state, dirty flags, and save/load operations.
"""

import os

class FileController:
    """
    Handles file opening, saving, and tab switching logic.
    Connects tab events to model file data.
    """

    def __init__(self, root_controller):
        self.root = root_controller
        self.model = root_controller.model.file

    def open_file(self, path):
        self.model.open(path)
        print(f"[FileController] Opened file: {path}")

    def mark_dirty(self, index):
        self.model.mark_dirty(index)
        print(f"[FileController] Marked file {index} as dirty")

    def save_file(self, index):
        self.model.save(index)

    def get_open_files(self):
        return self.model.open_files

    def get_active_file(self):
        if self.model.active_index is not None:
            return self.model.open_files[self.model.active_index]
        return None

    def is_valid(self):
        return not self.model.is_corrupt()