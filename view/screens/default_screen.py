"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines the DefaultScreen class, the primary screen for the application.
It initializes a tkinter Frame and integrates with the centralized frame management system.
"""

import tkinter as tk


class DefaultScreen(tk.Frame):
    """
    The main screen of the application, rendered after splash or project selection.
    Integrates with the centralized frame management system.
    """

    def __init__(self, parent, controller):
        """
        Initialize the DefaultScreen frame.

        :param parent: The parent widget where the frame is drawn.
        :param controller: The controller managing frame transitions.
        """
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Default Screen", font=("Arial", 16))
        label.pack(pady=10)

        button = tk.Button(self, text="Go to Project Screen",
                           command=lambda: controller.show_frame("ProjectScreen"))
        button.pack()
