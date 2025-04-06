"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.2.0

View is responsible for managing screen transitions and rendering.
"""

import tkinter as tk
from view.screens.splash_screen import SplashScreen
from view.screens.project_screen import ProjectScreen
from view.screens.default_screen import DefaultScreen
from view.screens.screen_manager import ScreenManager


class View:
    """
    The view manages all screen transitions and rendering.
    """

    def __init__(self, root, app_context):
        self.root = root
        self.app_context = app_context
        self.screen_manager = ScreenManager(root)

        self.app_context.view = self  # Injecting the view into the app context

        # Register the screens
        self._register_screens()

    def _register_screens(self):
        """
        Register all screens (Splash, Project, and Default).
        """
        self.screen_manager.register("SplashScreen", SplashScreen(self.app_context, self.root))
        self.screen_manager.register("ProjectScreen", ProjectScreen(self.app_context))
        self.screen_manager.register("DefaultScreen", DefaultScreen(self.app_context))

    def show_screen(self, name):
        """
        Show a specific screen by name.

        :param name: The name of the screen to show
        """
        self.screen_manager.show(name)

    def render(self, screen_name):
        """
        This method calls the render method of the appropriate screen.

        :param screen_name: Name of the screen to render
        """
        screen = self.screen_manager.get_screen(screen_name)
        if screen:
            screen.render(self.root)
