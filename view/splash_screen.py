"""
Author: Borgar Flaen Stensrud
Date: 2025-04-07
Version: 1.0.0

This module defines SplashScreen, which displays a splash screen with animations.
"""

import tkinter as tk
from PIL import ImageTk, Image
import os, time

class SplashScreen(tk.Toplevel):
    """
    Displays a splash screen with animations.
    """

    def __init__(self, root, controller):
        super().__init__(root)
        self.root = root
        self.controller = controller

        self.overrideredirect(True)
        self.configure(bg="black")
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-transparentcolor", "black")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")

        self.canvas = tk.Canvas(self, width=screen_width, height=screen_height, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.controller.initialize_splash(self)

    def start_animation(self):
        """Starts the splash screen animation."""
        self.controller.start_splash_animation(self)

    def cleanup(self):
        """Cleans up the splash screen and notifies the controller."""
        self.destroy()
        self.controller.on_splash_complete(self.root)