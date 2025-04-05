import tkinter as tk
from tkinter import ttk

class ThemeManager:
    def __init__(self, root):
        self.root = root
        self.style = ttk.Style(self.root)

        # Use 'clam' for better customization
        self.style.theme_use('clam')

        self.colors = {
            "bg": "#1e1e2e",
            "fg": "#f8f8f2",
            "accent": "#00ffe1",
            "highlight": "#00ccff",
            "button_bg": "#2e2e3e",
            "button_hover": "#3a3a4e",
            "entry_bg": "#2a2a3a",
            "border": "#44475a",
            "danger": "#ff5555"
        }

        self.fonts = {
            "base": ("Segoe UI", 10),
            "title": ("Segoe UI", 12, "bold")
        }

        self._apply_styles()

    def _apply_styles(self):
        # Global frame style
        self.style.configure("TFrame", background=self.colors["bg"])

        # Labels
        self.style.configure("TLabel", background=self.colors["bg"], foreground=self.colors["fg"], font=self.fonts["base"])

        # Buttons
        self.style.configure("TButton",
                             background=self.colors["button_bg"],
                             foreground=self.colors["fg"],
                             borderwidth=0,
                             padding=6,
                             font=self.fonts["base"])
        self.style.map("TButton",
                       background=[("active", self.colors["button_hover"])],
                       foreground=[("active", self.colors["accent"])])

        # Entries
        self.style.configure("TEntry",
                             fieldbackground=self.colors["entry_bg"],
                             foreground=self.colors["fg"],
                             padding=5,
                             borderwidth=1)

        # ComboBox
        self.style.configure("TCombobox",
                             fieldbackground=self.colors["entry_bg"],
                             background=self.colors["entry_bg"],
                             foreground=self.colors["fg"],
                             borderwidth=1,
                             padding=5)

    def apply_to_root(self):
        self.root.configure(bg=self.colors["bg"])
