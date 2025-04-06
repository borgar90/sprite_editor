"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines ToolModel, which manages the active tool, selection, and tool-related state.
"""

class ToolModel:
    """
    Tracks current tool selection and cursor/interaction state.
    Includes selected tile, region, or multi-tile selection.
    """

    def __init__(self, root_model):
        self.root = root_model
        self.active_tool = "Select"
        self.selected_cell = None  # (row, col)
        self.selected_area = None  # (row1, col1, row2, col2) for drag box

    def select_tool(self, tool_name):
        self.active_tool = tool_name

    def select_cell(self, row, col):
        self.selected_cell = (row, col)
        self.selected_area = None

    def select_area(self, r1, c1, r2, c2):
        self.selected_area = (r1, c1, r2, c2)
        self.selected_cell = None

    def clear_selection(self):
        self.selected_cell = None
        self.selected_area = None

    def serialize(self):
        return {
            "active_tool": self.active_tool,
            "selected_cell": self.selected_cell,
            "selected_area": self.selected_area
        }

    def load(self, data):
        self.active_tool = data.get("active_tool", "Select")
        self.selected_cell = data.get("selected_cell", None)
        self.selected_area = data.get("selected_area", None)

    def is_corrupt(self):
        return False