"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines CoreLayout, the layout used by the CoreFunctionsScreen.
It arranges the full editing UI: top menu, project bar, canvas, tools, and properties.
"""

import tkinter as tk
from view.layouts.base_layout import BaseLayout
from view.sections.file_menu_section import FileMenuSection
from view.sections.project_bar_section import ProjectBarSection
from view.sections.infinite_canvas_section import InfiniteCanvasSection
from view.sections.tool_properties_section import ToolPropertiesSection
from view.sections.tool_menu_section import ToolMenuSection


class CoreLayout(BaseLayout):
    """
    Layout that composes all UI sections for the core editing screen.
    Organizes menu, bar, canvas, tools, and right-side panel.
    """

    def render(self):
        # Clear and build full layout
        self.root.grid_rowconfigure(2, weight=1)  # Main body row
        self.root.grid_columnconfigure(0, weight=1)  # Canvas area

        # --- Top Menu ---
        file_menu = FileMenuSection("FileMenu")
        file_menu.render(self.root, row=0, column=0, columnspan=2, sticky="ew")

        # --- Project Bar ---
        project_bar = ProjectBarSection("ProjectBar")
        project_bar.render(self.root, row=1, column=0, columnspan=2, sticky="ew")

        # --- Canvas ---
        canvas_section = InfiniteCanvasSection("Canvas")
        canvas_section.render(self.root, row=2, column=0, sticky="nsew")

        # --- Properties Panel ---
        properties_panel = ToolPropertiesSection("ToolProps")
        properties_panel.render(self.root, row=2, column=1, sticky="ns")

        # --- Floating Toolbar ---
        tool_menu = ToolMenuSection("ToolMenu")
        tool_menu.render(canvas_section.frame)  # Overlay on canvas