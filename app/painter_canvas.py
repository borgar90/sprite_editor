import tkinter as tk
from PIL import ImageTk

class PainterCanvas:
    def __init__(self, parent_frame, app_logic, tile_size=32, rows=16, cols=16):
        self.app_logic = app_logic
        self.tile_size = tile_size
        self.rows = rows
        self.cols = cols

        self.canvas = tk.Canvas(
            parent_frame,
            width=cols * tile_size,
            height=rows * tile_size,
            bg="#1e1e2e",  # Dark background
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
        if not self.selected_tile:
            return

        tile_id, pil_img, layer = self.selected_tile
        col = event.x // self.tile_size
        row = event.y // self.tile_size

        if (col, row) not in self.tilemap:
            return

        self.tilemap[(col, row)][layer] = tile_id

        # Cache and draw image
        key = (tile_id, layer)
        if key not in self.tile_images:
            resized = pil_img.resize((self.tile_size, self.tile_size))
            self.tile_images[key] = ImageTk.PhotoImage(resized)

        img = self.tile_images[key]
        self.canvas.create_image(
            col * self.tile_size,
            row * self.tile_size,
            image=img,
            anchor="nw",
            tags=f"{col}-{row}-{layer}"
        )

    def _erase(self, event):
        col = event.x // self.tile_size
        row = event.y // self.tile_size

        if (col, row) not in self.tilemap:
            return

        # Remove all layers for that tile
        for layer in self.tilemap[(col, row)]:
            self.tilemap[(col, row)][layer] = None
            self.canvas.delete(f"{col}-{row}-{layer}")

    def set_selected_tile(self, tile_id, pil_image, layer):
        self.selected_tile = (tile_id, pil_image, layer)
