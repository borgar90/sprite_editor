"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines the BaseLayout class, which provides a base for GUI layout management.
Layouts are responsible for arranging sections on the screen using a chosen geometry manager.
"""

from abc import ABC, abstractmethod


class BaseLayout(ABC):
    """
    Abstract base class for layout managers.
    A layout is responsible for positioning sections (e.g., left panel, right panel) on the root window or screen.
    """

    def __init__(self, root):
        """
        Initialize the layout manager.

        :param root: The root widget or screen container where layout is applied.
        """
        self.root = root
        self.sections = []  # List of BaseSection instances

    def add_section(self, section, **options):
        """
        Add a section to the layout.

        :param section: An instance of BaseSection
        :param options: Keyword arguments for layout configuration (e.g., grid, pack)
        """
        self.sections.append((section, options))

    @abstractmethod
    def render(self):
        """
        Abstract method to render the layout and place all sections.
        Subclasses should implement layout strategy (grid, pack, place).
        """
        pass

    def destroy(self):
        """
        Destroy all sections in this layout.
        """
        for section, _ in self.sections:
            section.destroy()
        self.sections.clear()