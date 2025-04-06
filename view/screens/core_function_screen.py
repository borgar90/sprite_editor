"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines CoreFunctionsScreen, the main editing interface of the sprite editor.
It includes a file menu, project bar, infinite canvas, tool panel, and dynamic properties panel.
"""

import tkinter as tk
from view.screens.base_screen import BaseScreen
from view.layouts.core_layout import CoreLayout


class CoreFunctionsScreen(BaseScreen):
    """
    Main editor screen of the application.
    This screen contains all the core functionality: canvas, tools, properties, and file/project menus.
    """

    def render(self, root):
        """
        Render the screen by creating the layout and all of its sections.

        :param root: The root window container
        """
        self.layout = CoreLayout(root)
        self.layout.render()
