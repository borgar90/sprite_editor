"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.2.0

Main entry point for the Sprite Editor application.
Hands off setup responsibility to Controller to enforce MVC boundaries.
"""

import tkinter as tk
from controller.controller import Controller
from init import INITApp
from model.model import Model  # Make sure the model is imported first
from view.screens.default_screen import DefaultScreen
from view.screens.project_screen import ProjectScreen
from view.screens.splash_screen import SplashScreen


class AppContext:
    """
    Shared dependency context between all major layers.
    """
    def __init__(self):
        self.model = None
        self.controller = None
        self.view = None
        self.selected_project = None


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sprite Editor")
        self.geometry("1280x800")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (SplashScreen, ProjectScreen, DefaultScreen):
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("SplashScreen")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def start_splash(self):
        self.after(3000, lambda: self.show_frame("ProjectScreen"))  # Show ProjectScreen after 3 seconds


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
