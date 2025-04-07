"""
Author: Borgar Flaen Stensrud
Date: 2025-04-07
Version: 1.0.0

This module defines PalettePanel, which manages a palette of tiles.
"""

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class PalettePanel(BaseView):
    """
    Manages a palette of tiles.
    """

    def __init__(self, parent_frame, controller):
        super().__init__(parent_frame)
        self.controller = controller
        self.tile_size = 32
        self.tiles = []
        self.tile_images = []
        self.selected_tile_id = None

        self._build_ui()
        self.controller.load_default_palette(self)

    def _build_ui(self):
        control_frame = tk.Frame(self.frame, bg="#1e1e2e")
        control_frame.pack(fill="x", pady=5, padx=5)

        tk.Button(control_frame, text="Load Image", command=self.controller.load_image).pack(side="left", padx=5)

        tk.Label(control_frame, text="Layer:").pack(side="left", padx=(10, 0))
        self.layer = tk.StringVar(value="base")
        tk.OptionMenu(control_frame, self.layer, "base", "overlay", "decoration").pack(side="left")

        self.swatch_canvas = tk.Canvas(self.frame, height=200, bg="#1e1e2e", highlightthickness=0)
        self.swatch_frame = tk.Frame(self.swatch_canvas, bg="#1e1e2e")
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.swatch_canvas.yview)
        self.swatch_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.swatch_canvas.pack(side="left", fill="both", expand=True)
        self.swatch_canvas.create_window((0, 0), window=self.swatch_frame, anchor="nw")
        self.swatch_frame.bind("<Configure>", lambda e: self.swatch_canvas.configure(scrollregion=self.swatch_canvas.bbox("all")))