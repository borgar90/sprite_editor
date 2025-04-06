# gui_elements/grid_preview_renderer.py
from PIL import ImageTk
import tkinter as tk

class GridPreviewRenderer:
    def __init__(self, canvas, grid_container, app_logic, zoom_level):
        self.canvas = canvas
        self.grid_container = grid_container
        self.app_logic = app_logic
        self.zoom_level = zoom_level

    def render(self):
        self.canvas.delete("all")
        for widget in self.grid_container.winfo_children():
            widget.destroy()

        tw = self.app_logic.tile_width
        th = self.app_logic.tile_height
        cols = self.app_logic.grid_cols
        rows = self.app_logic.grid_rows
        zoom = self.zoom_level

        tile_w = int(tw * zoom)
        tile_h = int(th * zoom)

        img_width = cols * tile_w
        img_height = rows * tile_h

        if self.app_logic.image:
            img = self.app_logic.image.copy().resize((img_width, img_height))
            self._tk_image = ImageTk.PhotoImage(img)
            tk.Label(self.grid_container, image=self._tk_image, bg="#2a2a2a").place(x=0, y=0)

        self.grid_container.config(width=img_width, height=img_height)
        self.canvas.itemconfig(self.canvas.create_window(0, 0, anchor="nw", window=self.grid_container),
                               width=img_width, height=img_height)

        for x in range(0, img_width + 1, tile_w):
            self.canvas.create_line(x, 0, x, img_height, fill="#555")
        for y in range(0, img_height + 1, tile_h):
            self.canvas.create_line(0, y, img_width, y, fill="#555")

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.update_idletasks()
