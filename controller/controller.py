"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.2.0

Controller handles app logic, triggering the appropriate screens.
"""

from view.view import View
from controller.project.project_controller import ProjectController
from model.model import Model
from controller.app_state import AppState

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


        # Initialize AppState
        self.app_state = AppState()
        self.app_context.app_state = self.app_state

        # Add listener to handle state changes
        self.app_state.add_listener(self.handle_state_change)

    def start(self):
        """
        Starts the application by showing the splash screen.
        """
        # Start with the splash screen only
        self.app_context.app_state.set_state("splash")

    def handle_state_change(self, new_state):
        """
        Handles the change in app state, triggering screen transitions.
        """
        if new_state == "splash":
            self.view.show_screen("SplashScreen")
        elif new_state == "project":
            self.view.app_context.root.deiconify()
            self.view.show_screen("ProjectScreen")

    def _on_splash_complete(self):
        """
        Callback to show the project selection screen after splash completes.
        """
        self.view.show_screen("ProjectScreen")
