# view/elements/gui_element.py
from abc import ABC, abstractmethod
import tkinter as tk


class GUIElement(ABC):
    def __init__(self, parent):
        self.parent = parent
        self.widget = None  # This will hold the actual tk/ttk widget

    @abstractmethod
    def render(self, **pack_args):
        pass

    def destroy(self):
        if self.widget:
            self.widget.destroy()
