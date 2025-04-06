"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines the BaseScreen class, which represents a complete screen in the GUI.
Each screen manages its own layout, sections, and lifecycle (rendering, unmounting, destruction).
"""

from abc import ABC, abstractmethod


class BaseScreen(ABC):
    """
    Abstract base class for all screens in the application.
    A screen is a full-page view that manages its own layout and content lifecycle.
    """

    def __init__(self, app_context):
        """
        Initialize the screen with application context.

        :param app_context: Global application state or context shared across screens.
        """
        self.app_context = app_context
        self.layout = None  # Expected to be an instance of BaseLayout or subclass

    # Optional render method; it can be overridden in specific screens
    def render(self, root):
        pass  # Let View handle rendering logic

    def unmount(self):
        """
        Optional hook called before the screen is removed or hidden.
        Can be overridden to pause logic or save state.
        """
        pass

    def destroy(self):
        """
        Destroy the screen and cleanup any associated widgets or layout.
        """
        if self.layout:
            self.layout.destroy()
            self.layout = None
