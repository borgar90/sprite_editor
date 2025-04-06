"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines the BaseSection class, which provides a reusable base for GUI sections.
Sections represent logical areas of the screen (e.g., left panel, right panel, canvas)
and should only handle GUI concerns, not business logic.
"""

from abc import ABC, abstractmethod


class BaseSection(ABC):
    """
    Base class for all GUI sections.
    A section is a logical division of the GUI, such as a panel or container area,
    responsible for holding widgets or layout elements.
    """

    def __init__(self, name: str):
        """
        Initialize the section with a name.

        :param name: Identifier name for the section
        """
        self.name = name
        self.frame = None  # This will be a tk.Frame or ttk.Frame injected on render
        self.elements = []  # List of BaseElement instances

    @abstractmethod
    def render(self, parent, **options):
        """
        Render the section into the given parent widget.

        :param parent: The parent Tkinter widget or layout element.
        :param options: Optional keyword arguments for rendering configuration.
        """
        pass

    def destroy(self):
        """
        Destroy the section and clean up any associated resources.
        """
        if self.frame:
            self.frame.destroy()
            self.frame = None

    def add_element(self, element):
        """
        Add a GUI element to the section.

        :param element: An instance of BaseElement or subclass.
        """
        self.elements.append(element)
        if self.frame:
            element.render(self.frame)

    def clear_elements(self):
        """
        Destroy and remove all child elements from the section.
        """
        for element in self.elements:
            element.destroy()
        self.elements.clear()
