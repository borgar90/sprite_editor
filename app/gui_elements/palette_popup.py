# app/gui_elements/palette_popup.py
from .gui_element import GUIElement
import tkinter as tk
from app.palette_panel import PalettePanel

class PalettePopup(GUIElement):
    def __init__(self, root, app_logic, on_tile_selected):
        super().__init__(root, app_logic)
        self.on_tile_selected = on_tile_selected

    def open(self):
        popup = tk.Toplevel(self.root)
        popup.title("Palette Editor")
        popup.configure(bg="#1e1e2e")
        popup.geometry("640x400")
        popup.minsize(400, 300)

        popup.transient(self.root)
        popup.grab_set()

        PalettePanel(popup, self.app_logic, self.on_tile_selected)
