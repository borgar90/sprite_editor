import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

from app.widgets import (
    create_button,
    create_label,
    create_combobox,
)
from app.theme import ThemeManager  # Optional, for color reference if needed

class PalettePanel:
    def __init__(self, parent_frame, app_logic, on_tile_selected):
        self.frame = tk.Frame(parent_frame, bg="#1e1e2e")
        self.frame.pack(fill="both", expand=True)

        self.app_logic = app_logic
        self.on_tile_selected = on_tile_selected
        self.tile_size = 32
        self.tiles = []
        self.tile_images = []
        self.selected_tile_id = None
        self.layer = tk.StringVar(value="base")

        self._build_ui()
        self._load_default_rgb_palette()

    def _build_ui(self):
        control_frame = tk.Frame(self.frame, bg="#1e1e2e")
        control_frame.pack(fill="x", pady=5, padx=5)

        create_button(control_frame, text="Load Image", command=self._load_image).pack(side="left", padx=5)

        create_label(control_frame, text="Layer:").pack(side="left", padx=(10, 0))
        create_combobox(control_frame, values=["base", "overlay", "decoration"], variable=self.layer).pack(side="left")

        # Scrollable swatch area
        self.swatch_canvas = tk.Canvas(self.frame, height=200, bg="#1e1e2e", highlightthickness=0)
        self.swatch_frame = tk.Frame(self.swatch_canvas, bg="#1e1e2e")
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.swatch_canvas.yview)
        self.swatch_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.swatch_canvas.pack(side="left", fill="both", expand=True)
        self.swatch_canvas.create_window((0, 0), window=self.swatch_frame, anchor="nw")
        self.swatch_frame.bind("<Configure>", lambda e: self.swatch_canvas.configure(scrollregion=self.swatch_canvas.bbox("all")))

    def _load_default_rgb_palette(self):
        colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "gray", "white", "black"]
        for color in colors:
            img = Image.new("RGBA", (self.tile_size, self.tile_size), color)
            self._add_tile(img, label=color)

    def _load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
        if not path:
            return

        img = Image.open(path)
        w, h = img.size
        tw, th = self.tile_size, self.tile_size

        index = len(self.tiles)
        for y in range(0, h, th):
            for x in range(0, w, tw):
                tile = img.crop((x, y, x + tw, y + th))
                self._add_tile(tile, label=f"{os.path.basename(path)}_{index}")
                index += 1

    def _add_tile(self, pil_tile, label=""):
        tile_id = len(self.tiles)
        self.tiles.append((tile_id, pil_tile))

        tk_img = ImageTk.PhotoImage(pil_tile.resize((32, 32)))
        self.tile_images.append(tk_img)

        btn = tk.Button(self.swatch_frame, image=tk_img, relief="flat",
                        command=lambda i=tile_id: self._select_tile(i))

        btn.grid(row=tile_id // 6, column=tile_id % 6, padx=2, pady=2)

    def _select_tile(self, tile_id):
        self.selected_tile_id = tile_id
        image = self.tiles[tile_id][1]
        layer = self.app_logic.current_layer
        self.on_tile_selected(tile_id, image, layer)

