# view/sections/section.py
import tkinter as tk

class Section:
    def __init__(self, parent: tk.Widget):
        self.parent = parent
        self.frame = tk.Frame(parent, bg="#2a2a2a")

    def render(self, **pack_options):
        self.frame.pack(**pack_options)

    def destroy(self):
        self.frame.destroy()


