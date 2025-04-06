"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines AssetsModel, which tracks user-imported and default assets
available for the palette, canvas, or animations.
"""

import os

class AssetsModel:
    """
    Manages visual assets (images, sprites) loaded into the project.
    These assets may appear in palette, be painted on grid, or used for previews.
    """

    def __init__(self, root_model):
        self.root = root_model
        self.assets = {}  # id → asset metadata

    def add_asset(self, asset_id, path, scale=1.0):
        """
        Register a new visual asset by ID.

        :param asset_id: Unique identifier (e.g. filename)
        :param path: Absolute or relative path to image file
        :param scale: Optional scale multiplier
        """
        if os.path.exists(path):
            self.assets[asset_id] = {
                "path": path,
                "scale": scale
            }

    def get_asset(self, asset_id):
        return self.assets.get(asset_id, None)

    def remove_asset(self, asset_id):
        self.assets.pop(asset_id, None)

    def serialize(self):
        return {"assets": self.assets.copy()}

    def load(self, data):
        self.assets = data.get("assets", {})

    def is_corrupt(self):
        return not isinstance(self.assets, dict)