"""
Author: Borgar Flaen Stensrud
Date: 2025-04-07
Version: 1.0.0

This module defines BaseView, which provides a foundation for all view classes.
It ensures consistent theme application and provides utility methods for creating styled widgets.
"""

import tkinter as tk
from tkinter import ttk
from view.theme_manager import ThemeManager

class BaseView:
    """
    Provides a foundation for all view classes.
    """

    def __init__(self, root):
        self.root = root
        self.theme_manager = ThemeManager(self.root)
        self.theme_manager.apply_to_root()

    def create_button(self, text, command, style="TButton"):
        """Creates a styled button."""
        return ttk.Button(self.root, text=text, command=command, style=style)

    def create_label(self, text, style="TLabel"):
        """Creates a styled label."""
        return ttk.Label(self.root, text=text, style=style)

    def create_entry(self, textvariable, style="TEntry"):
        """Creates a styled entry widget."""
        return ttk.Entry(self.root, textvariable=textvariable, style=style)

    def create_combobox(self, values, textvariable, style="TCombobox"):
        """Creates a styled combobox."""
        return ttk.Combobox(self.root, values=values, textvariable=textvariable, style=style)

"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.2.0

View is responsible for managing screen transitions and rendering.
"""

from view.screens.splash_screen import SplashScreen
from view.screens.project_screen import ProjectScreen
from view.screens.default_screen import DefaultScreen
from view.screens.screen_manager import ScreenManager


class View(BaseView):
    """
    The view manages all screen transitions and rendering.
    """

    def __init__(self, root, app_context):
        super().__init__(root)
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
        # Pass the loaded projects to the ProjectScreen
        self.screen_manager.register("ProjectScreen", ProjectScreen(self.app_context, projects=self.app_context.projects))
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
