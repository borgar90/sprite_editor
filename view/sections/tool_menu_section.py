"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This section defines ToolMenuSection, a floating vertical tool selector menu
anchored to the left side of the canvas inside the InfiniteCanvasSection.
"""

import tkinter as tk
from view.sections.base_section import BaseSection


class ToolMenuSection(BaseSection):
    """
    Floating vertical menu on the far left of the canvas.
    Lets users choose an active tool (e.g. select, draw, erase, inspect).
    """

    def render(self, parent, **options):
        self.frame = tk.Frame(parent, bg="#151515")
        self.frame.place(x=0, y=0, relheight=1, width=60)

        tools = ["Select", "Draw", "Erase", "Inspect"]

        for tool in tools:
            btn = tk.Button(
                self.frame,
                text=tool,
                width=8,
                bg="#303030",
                fg="white",
                relief="flat",
                command=lambda t=tool: self.select_tool(t)
            )
            btn.pack(pady=10, padx=5)

    def select_tool(self, tool):
        """
        Tool selection handler.
        Will later dispatch tool state to controller or context.
        """
        print(f"[ToolMenu] Tool selected: {tool}")
