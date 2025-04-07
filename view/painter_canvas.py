"""
Author: Borgar Flaen Stensrud
Date: 2025-04-07
Version: 1.0.0

This module defines PainterCanvas, which provides a grid-based canvas for painting tiles.
"""

import tkinter as tk
from PIL import ImageTk
from view.view import BaseView  # Import BaseView to resolve the NameError

class PainterCanvas(BaseView):
    """
    Provides a grid-based canvas for painting tiles.
    """

    def __init__(self, parent_frame, controller, tile_size=32, rows=16, cols=16):
        super().__init__(parent_frame)
        self.controller = controller
        self.tile_size = tile_size
        self.rows = rows
        self.cols = cols

        self.canvas = tk.Canvas(
            self.root,
            width=cols * tile_size,
            height=rows * tile_size,
            bg=self.theme_manager.colors["bg"],
            highlightthickness=0,
            bd=0
        )
        self.canvas.pack(fill="both", expand=True)

        self.selected_tile = None
        self.tilemap = self._init_tilemap()
        self.tile_images = {}

        self._draw_grid()

        self.canvas.bind("<Button-1>", self._paint)
        self.canvas.bind("<Button-3>", self._erase)

    def _init_tilemap(self):
        return {
            (x, y): {"base": None, "overlay": None, "decoration": None}
            for x in range(self.cols) for y in range(self.rows)
        }

    def _draw_grid(self):
        for x in range(self.cols):
            for y in range(self.rows):
                self.canvas.create_rectangle(
                    x * self.tile_size,
                    y * self.tile_size,
                    (x + 1) * self.tile_size,
                    (y + 1) * self.tile_size,
                    outline="#2f2f3f"  # Soft neon grid color
                )

    def _paint(self, event):
        self.controller.paint_tile(event, self.tile_size, self.tilemap, self.tile_images, self.canvas)

    def _erase(self, event):
        self.controller.erase_tile(event, self.tile_size, self.tilemap, self.canvas)

    def set_selected_tile(self, tile_id, pil_image, layer):
        self.selected_tile = (tile_id, pil_image, layer)