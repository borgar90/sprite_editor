"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

CanvasSection represents a scrollable or interactive canvas area
inside the GUI. It uses a custom PainterCanvas for rendering and user interactions.
"""

from abc import ABC
from view.sections.base_section import BaseSection
from view.painter_canvas import PainterCanvas  # Corrected import path


class CanvasSection(BaseSection, ABC):
    """
    Represents a reusable section for drawing and interacting with the canvas.
    """

    def __init__(self, parent, app_logic):
        """
        Initialize the canvas section.

        :param parent: The parent widget or container
        :param app_logic: Reference to the application's controller or logic layer
        """
        super().__init__(parent, app_logic)
        self.canvas = PainterCanvas(self.frame, app_logic)  # Attach PainterCanvas to this section's frame

    def get_canvas(self):
        """
        Returns the internal PainterCanvas instance for direct interaction.
        """
        return self.canvas
