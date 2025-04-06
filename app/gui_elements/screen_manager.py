# app/gui_elements/screen_manager.py
from gui_element import GUIElement
import tkinter as tk
from tkinter import ttk

class ScreenManager(GUIElement):
    def __init__(self, root, app_logic, mode_label_ref):
        super().__init__(root, app_logic)
        self.mode_label = mode_label_ref
        self.preview_container = None
        self.paint_container = None

    def init_widgets(self, parent_frame):
        self.paint_container = ttk.Frame(parent_frame)
        self.preview_container = ttk.Frame(parent_frame)

        self.painter = self.app_logic.painter_class(self.paint_container, self.app_logic)

        return self.paint_container, self.preview_container

    def switch_to(self, screen):
        self.preview_container.pack_forget()
        self.paint_container.pack_forget()

        if screen == "paint":
            self.paint_container.pack(side="left", fill="both", expand=True, padx=10, pady=10)
            self.mode_label.config(text="🛠️ Painter Mode")
        elif screen == "preview":
            self.preview_container.pack(side="left", fill="both", expand=True, padx=10, pady=10)
            self.mode_label.config(text="🔍 Preview Mode")
