"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines the DefaultScreen class, the primary screen for the application.
It initializes a GridLayout and renders left panel, main canvas, and right panel sections.
"""

from view.screens.base_screen import BaseScreen
from view.layouts.grid_layout import GridLayout
from view.sections.left_panel_section import LeftPanelSection
from view.sections.canvas_section import CanvasSection
from view.sections.right_panel_section import RightPanelSection


class DefaultScreen(BaseScreen):
    """
    The main screen of the application, rendered after splash or project selection.
    Composed of left, center (canvas), and right sections arranged in a GridLayout.
    """

    def render(self, root):
        """
        Render the screen using a GridLayout with three sections.

        :param root: The root widget where the screen is drawn.
        """
        self.layout = GridLayout(root)

        left_section = LeftPanelSection("LeftPanel")
        canvas_section = CanvasSection("MainCanvas")
        right_section = RightPanelSection("RightPanel")

        self.layout.add_section(left_section, row=0, column=0, sticky="ns")
        self.layout.add_section(canvas_section, row=0, column=1, sticky="nsew")
        self.layout.add_section(right_section, row=0, column=2, sticky="ns")

        self.layout.render()

    def unmount(self):
        # Optional cleanup before switching away from this screen
        pass
