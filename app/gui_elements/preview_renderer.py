# app/gui_elements/preview_renderer.py
from gui_element import GUIElement
from PIL import ImageTk
import tkinter as tk

class PreviewRenderer(GUIElement):
    def __init__(self, root, app_logic, preview_canvas, grid_container, grid_window, zoom_level_getter):
        super().__init__(root, app_logic)
        self.preview_canvas = preview_canvas
        self.grid_container = grid_container
        self.grid_window = grid_window
        self.get_zoom_level = zoom_level_getter
        self._tk_image = None

    def render(self):
        self.preview_canvas.delete("all")
        for widget in self.grid_container.winfo_children():
            widget.destroy()

        tw, th = self.app_logic.tile_width, self.app_logic.tile_height
        cols, rows = self.app_logic.grid_cols, self.app_logic.grid_rows
        zoom = self.get_zoom_level()

        tile_w, tile_h = int(tw * zoom), int(th * zoom)
        img_width, img_height = cols * tile_w, rows * tile_h

        if self.app_logic.image:
            img = self.app_logic.image.copy()
            img = img.resize((int(img.width * zoom), int(img.height * zoom)))
            self._tk_image = ImageTk.PhotoImage(img)

            label = tk.Label(self.grid_container, image=self._tk_image, bg="#2a2a2a")
            label.place(x=0, y=0)
            img_width, img_height = img.width, img.height

        self.grid_container.config(width=img_width, height=img_height)
        self.preview_canvas.coords(self.grid_window, 0, 0)
        self.preview_canvas.itemconfig(self.grid_window, width=img_width, height=img_height)

        for x in range(0, img_width + 1, tile_w):
            self.preview_canvas.create_line(x, 0, x, img_height, fill="#555")

        for y in range(0, img_height + 1, tile_h):
            self.preview_canvas.create_line(0, y, img_width, y, fill="#555")

        self.preview_canvas.configure(scrollregion=self.preview_canvas.bbox("all"))
        self.preview_canvas.update_idletasks()
