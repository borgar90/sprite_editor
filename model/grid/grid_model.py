"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines GridModel, which represents the tile grid inside the infinite canvas.
It stores grid dimensions, origin offset, and per-cell tile data.
"""

class GridModel:
    """
    Represents a single grid instance on the canvas.
    Stores tile data, dimensions, and spatial offset from canvas center.
    """

    def __init__(self, root_model):
        self.root = root_model
        self.rows = 10
        self.cols = 10
        self.tile_size = 32
        self.offset_x = 0  # relative to canvas center
        self.offset_y = 0

        # 2D grid (row-major), default is None or empty tile
        self.cells = [[None for _ in range(self.cols)] for _ in range(self.rows)]

    def set_cell(self, row, col, tile_data):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.cells[row][col] = tile_data

    def get_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.cells[row][col]
        return None

    def serialize(self):
        return {
            "rows": self.rows,
            "cols": self.cols,
            "tile_size": self.tile_size,
            "offset_x": self.offset_x,
            "offset_y": self.offset_y,
            "cells": self.cells  # can be optimized later
        }

    def load(self, data):
        self.rows = data.get("rows", 10)
        self.cols = data.get("cols", 10)
        self.tile_size = data.get("tile_size", 32)
        self.offset_x = data.get("offset_x", 0)
        self.offset_y = data.get("offset_y", 0)
        self.cells = data.get("cells", [[None for _ in range(self.cols)] for _ in range(self.rows)])

    def is_corrupt(self):
        return not isinstance(self.cells, list) or len(self.cells) != self.rows