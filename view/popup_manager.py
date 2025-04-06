"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines PopupManager, responsible for rendering and destroying
popup windows and tool overlays in the application.
"""

import tkinter as tk


class PopupManager:
    """
    Handles rendering and dismissal of transient popup windows.
    Optionally blocks background screen interaction.
    """

    def __init__(self, root):
        """
        Initialize the popup manager.

        :param root: The application's main root window
        """
        self.root = root
        self.popup = None

    def show_popup(self, content_builder, modal=True):
        """
        Display a popup with custom content.

        :param content_builder: Callable that accepts the Toplevel popup window
        :param modal: If True, popup disables interaction with root
        """
        if self.popup:
            self.close()

        self.popup = tk.Toplevel(self.root)
        self.popup.transient(self.root)
        self.popup.configure(bg="black")
        self.popup.grab_set() if modal else None

        content_builder(self.popup)

    def close(self):
        """
        Close and destroy the current popup.
        """
        if self.popup:
            self.popup.destroy()
            self.popup = None