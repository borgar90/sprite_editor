"""
Author: Borgar Flaen Stensrud
Date: 2025-04-07
Version: 1.0.0

This module defines ProjectSelector, which provides a GUI for selecting or creating a project.
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ProjectSelector:
    """
    Provides a GUI for selecting or creating a project.
    """

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.name_entry = tk.StringVar()

        self.popup = tk.Toplevel(root)
        self.popup.title("Select Project")
        self.popup.configure(bg="#1e1e2e")
        self.popup.resizable(False, False)

        self._center_popup(width=420, height=280)

        # Logo
        logo_img = Image.open("assets/splash/sprite_logo.png").resize((220, 66))
        logo_tk = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(self.popup, image=logo_tk, bg="#1e1e2e")
        logo_label.image = logo_tk
        logo_label.pack(pady=(20, 10))

        # Title
        tk.Label(
            self.popup,
            text="Select Project",
            fg="white",
            bg="#1e1e2e",
            font=("Arial", 14, "bold")
        ).pack(pady=(0, 10))

        # Buttons
        tk.Button(self.popup, text="📁 Open Existing Project", command=self.controller.open_project).pack(pady=5)
        tk.Button(self.popup, text="🆕 Start New Project", command=self.controller.new_project).pack(pady=5)

        self.popup.transient(root)
        self.popup.grab_set()
        self.popup.focus_force()

    def _center_popup(self, width, height):
        """Centers the popup window on the screen."""
        self.popup.update_idletasks()
        screen_w = self.popup.winfo_screenwidth()
        screen_h = self.popup.winfo_screenheight()
        x = (screen_w - width) // 2
        y = (screen_h - height) // 2
        self.popup.geometry(f"{width}x{height}+{x}+{y}")