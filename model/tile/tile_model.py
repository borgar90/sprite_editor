"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines TileModel, which represents individual tile data stored in each grid cell.
Each tile may contain sprite reference, z-index, metadata, animation, and layer info.
"""

class TileModel:
    """
    Defines the structure of data stored in each cell of the grid.
    Also provides helpers to validate, build, or clean tile objects.
    """

    def __init__(self, root_model):
        self.root = root_model

    def create_tile(self, sprite_id, z=0, meta=None):
        """
        Create a tile object with standard structure.

        :param sprite_id: ID or name of the visual asset
        :param z: Drawing order depth
        :param meta: Optional metadata dictionary
        """
        return {
            "sprite": sprite_id,
            "z": z,
            "meta": meta or {}
        }

    def is_valid_tile(self, tile):
        return isinstance(tile, dict) and "sprite" in tile

    def serialize(self):
        """
        TileModel does not store state directly (utility class),
        but required by model manager interface.
        """
        return {}

    def load(self, data):
        pass

    def is_corrupt(self):
        return False