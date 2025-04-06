"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.2.0

ScreenManager is responsible for handling screen transitions.
"""

class ScreenManager:
    """
    Manages all screens and their transitions.
    """

    def __init__(self, root):
        self.root = root
        self.screens = {}

    def register(self, name, screen):
        """
        Register a screen by name.

        :param name: The name to identify the screen
        :param screen: The screen object to register
        """
        self.screens[name] = screen

    def get_screen(self, name):
        """
        Retrieve a screen by name.

        :param name: The name of the screen to retrieve
        :return: The screen object
        """
        return self.screens.get(name)

    def show(self, name):
        """
        Show the screen with the specified name.

        :param name: The name of the screen to show
        """
        screen = self.get_screen(name)
        if screen:
            screen.render(self.root)  # Calls the render method of the screen
