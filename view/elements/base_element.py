"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines the BaseElement class, which provides a reusable base for GUI elements.
Elements are the smallest visible units in the GUI (buttons, labels, inputs, etc.), and
should be composed inside sections.
"""

from abc import ABC, abstractmethod


class BaseElement(ABC):
    """
    Base class for all individual GUI elements.
    These represent widgets that are placed inside sections, such as buttons or labels.
    """

    def __init__(self, master=None, **kwargs):
        """
        Initialize the element with optional master and configuration options.

        :param master: The parent container (e.g., a Frame or Section)
        :param kwargs: Additional keyword arguments for widget customization
        """
        self.master = master
        self.widget = None  # Will hold the actual Tkinter widget
        self.kwargs = kwargs

    @abstractmethod
    def render(self, master=None):
        """
        Abstract render method to be implemented by subclasses.

        :param master: Optional master override (e.g., new parent frame)
        """
        pass

    def destroy(self):
        """
        Destroy the widget associated with this element, if it exists.
        """
        if self.widget:
            self.widget.destroy()
            self.widget = None
