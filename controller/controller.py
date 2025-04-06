"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.2.0

Controller handles app logic, triggering the appropriate screens.
"""

from view.view import View
from controller.project.project_controller import ProjectController
from model.model import Model

class Controller:
    """
    Manages the app's flow, screens, and interactions.
    """

    def __init__(self, app_context, root):
        self.app_context = app_context
        self.root = root
        self.model = Model()
        app_context.model = self.model
        self.view = View(root, app_context)
        self.project_controller = ProjectController(self)
        self.app_context.controller = self  # Inject the controller into app context

    def start(self):
        """
        Starts the application by showing the splash screen.
        """
        # Start with the splash screen only
        self.view.show_screen("SplashScreen")
        splash_screen = self.app_context.view.screen_manager.get_screen("SplashScreen")

        # Set the callback for when the splash screen animation is complete
        splash_screen.schedule_complete_callback(self._on_splash_complete)

    def _on_splash_complete(self):
        """
        Callback to show the project selection screen after splash completes.
        """
        self.view.show_screen("ProjectScreen")
