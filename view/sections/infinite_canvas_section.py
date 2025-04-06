"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This section defines InfiniteCanvasSection, which hosts a scrollable canvas
that simulates infinite space for placing and editing grids.
"""

import tkinter as tk
from view.sections.base_section import BaseSection


class InfiniteCanvasSection(BaseSection):
    """
    Section with a scrollable canvas simulating an infinite editing area.
    The visible grid is limited, but the canvas can be scrolled endlessly.
    """

    def render(self, parent, **options):
        self.frame = tk.Frame(parent, bg="#1e1e1e")
        self.frame.grid(**options, sticky="nsew")

        # Enable stretching
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(self.frame, bg="#1e1e1e", scrollregion=(-5000, -5000, 5000, 5000))
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.h_scroll = tk.Scrollbar(self.frame, orient="horizontal", command=self.canvas.xview)
        self.h_scroll.grid(row=1, column=0, sticky="ew")

        self.v_scroll = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.v_scroll.grid(row=0, column=1, sticky="ns")

        self.canvas.configure(xscrollcommand=self.h_scroll.set, yscrollcommand=self.v_scroll.set)

        # Placeholder: center a mock grid (can be replaced by actual render engine)
        self._draw_centered_grid()

    def _draw_centered_grid(self):
        """
        Draw a placeholder centered grid to simulate core editing area.
        """
        grid_size = 32
        rows = 10
        cols = 10
        start_x = -cols * grid_size // 2
        start_y = -rows * grid_size // 2

        for i in range(rows):
            for j in range(cols):
                x1 = start_x + j * grid_size
                y1 = start_y + i * grid_size
                x2 = x1 + grid_size
                y2 = y1 + grid_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="#555", fill="", width=1)
