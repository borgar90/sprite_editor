"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 2.0.0

This module defines the ProjectScreen class using the new centralized frame management system.
It composes a vertical layout with a top logo, scrollable project list section, and a create button section.
"""
import os
import tkinter as tk


class ProjectScreen(tk.Frame):
    """
    Project selection screen that allows the user to select or create a project.
    It now uses a frame to be a valid Tkinter widget.
    """

    def __init__(self, parent, controller):
        """
        Initialize the project screen with parent and controller.

        :param parent: The Tkinter parent widget (usually the root or main window)
        :param controller: The controller managing the application state and navigation
        """
        super().__init__(parent)
        self.controller = controller

        # Add a label to the screen
        label = tk.Label(self, text="Project Screen", font=("Arial", 16))
        label.pack(pady=10)

        # Add a button to navigate to the default screen
        button = tk.Button(
            self,
            text="Go to Default Screen",
            command=lambda: controller.show_frame("DefaultScreen")
        )
        button.pack()