"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This is the root model controller for the sprite editor application.
It initializes and coordinates all sub-models including project, file, grid, tool, and assets.
It also manages logging, state recovery, and access from controller/view layers.
"""
from model.project.project_model import ProjectModel
from model.file.file_model import FileModel
from model.grid.grid_model import GridModel
from model.tile.tile_model import TileModel
from model.tool.tool_model import ToolModel
from model.assets.assets_model import AssetsModel


class Model:
    """
    Central orchestrator for all model components.
    Provides access to project state, files, grid data, tools, and asset resources.
    Supports state logging and recovery from corruption.
    """

    def __init__(self):
        self.project = ProjectModel(self)
        self.file = FileModel(self)
        self.grid = GridModel(self)
        self.tile = TileModel(self)
        self.tool = ToolModel(self)
        self.assets = AssetsModel(self)

        self._state_log = []
        self._max_log_entries = 100

    def snapshot_state(self):
        """
        Capture a minimal state snapshot for recovery purposes.
        """
        snapshot = {
            "project": self.project.serialize(),
            "file": self.file.serialize(),
            "grid": self.grid.serialize(),
            "tool": self.tool.serialize(),
            "assets": self.assets.serialize()
        }
        self._state_log.append(snapshot)
        if len(self._state_log) > self._max_log_entries:
            self._state_log.pop(0)

    def detect_corruption(self):
        """
        Detect if any model components are in a corrupted state.
        This should be extended to verify structural integrity.
        """
        return any([
            self.project.is_corrupt(),
            self.file.is_corrupt(),
            self.grid.is_corrupt(),
            self.tool.is_corrupt(),
            self.assets.is_corrupt()
        ])

    def restore_last_valid_state(self):
        """
        Restore the most recent known-good snapshot.
        """
        for snapshot in reversed(self._state_log):
            if snapshot:
                self.project.load(snapshot["project"])
                self.file.load(snapshot["file"])
                self.grid.load(snapshot["grid"])
                self.tool.load(snapshot["tool"])
                self.assets.load(snapshot["assets"])
                print("[Model] Restored last known valid state.")
                break
