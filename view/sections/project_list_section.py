"""
Author: Borgar Flaen Stensrud
Date: 2025-04-06
Version: 1.0.0

This module defines the ProjectListSection class, which displays all available project tiles
alongside a FindProjectTileElement, inside a scrollable container.
"""

import tkinter as tk
from view.sections.base_section import BaseSection
from view.elements.project_tile_element import ProjectTileElement
from view.elements.find_project_tile_element import FindProjectTileElement


class ProjectListSection(BaseSection):
    """
    Section displaying a scrollable list of project tiles and a find-project tile.
    """

    def __init__(self, name, project_data, on_select, on_find):
        """
        Initialize the section.

        :param name: Identifier
        :param project_data: List of project dicts (title, img_path, path)
        :param on_select: Callback when a tile is selected
        :param on_find: Callback for find-project tile
        """
        super().__init__(name)
        self.project_data = project_data
        self.on_select = on_select
        self.on_find = on_find
        self.selected_tile = None

    def render(self, parent, **options):
        self.frame = tk.Frame(parent, bg="white", bd=2, relief="solid")
        self.frame.pack(**options, fill="both", expand=True)

        canvas = tk.Canvas(self.frame, bg="#1e1e1e", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=canvas.yview)
        scrollable = tk.Frame(canvas, bg="#1e1e1e")

        scrollable.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Add project tiles
        if self.project_data:
            for proj in self.project_data:
                tile = ProjectTileElement(
                    master=scrollable,
                    title=proj["title"],
                    img_path=proj["img_path"],
                    data=proj,
                    on_select=self._handle_select
                )
                tile.render()
                self.elements.append(tile)
        else:
            self._add_find_only(scrollable)

        # Always add find-project tile at end
        find_tile = FindProjectTileElement(scrollable, on_click=self.on_find)
        find_tile.render()
        self.elements.append(find_tile)

    def _handle_select(self, selected_element):
        if self.selected_tile:
            self.selected_tile.set_selected(False)
        self.selected_tile = selected_element
        self.selected_tile.set_selected(True)
        self.on_select(self.selected_tile.data)

    def _add_find_only(self, parent):
        placeholder = FindProjectTileElement(parent, on_click=self.on_find)
        placeholder.render()
        self.elements.append(placeholder)
