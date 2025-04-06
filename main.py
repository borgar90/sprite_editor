"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.2.0

Main entry point for the Sprite Editor application.
Hands off setup responsibility to Controller to enforce MVC boundaries.
"""

import tkinter as tk
from controller.controller import Controller
from model.model import Model  # Make sure the model is imported first


class AppContext:
    """
    Shared dependency context between all major layers.
    """
    def __init__(self):
        self.model = None
        self.controller = None
        self.view = None
        self.selected_project = None


def start_app():
    # 1. Initialize the root window for the app
    root = tk.Tk()
    root.title("Sprite Editor")
    root.geometry("1280x800")
    root.configure(bg="black")

    # Initially hide the main window until the splash screen is done
    root.withdraw()

    # 2. Initialize the app context and model first
    app = AppContext()
    app.model = Model()  # Initialize the model before the controller and view

    # 3. Initialize the controller, which will also set up the view
    app.controller = Controller(app, root)

    app.root = root
    # 4. Controller initializes view/model internally, and launches splash
    app.controller.start()

    root.mainloop()


if __name__ == "__main__":
    start_app()
