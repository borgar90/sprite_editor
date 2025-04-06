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

    def render(self, parent):
        """
        Render the project tiles and find-project tile into the parent container.
        """
        scrollable = tk.Frame(parent)
        scrollable.pack(fill="both", expand=True)

        # Add project tiles if there are any
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

        # Always add the "find project" tile at the end
        find_tile = FindProjectTileElement(scrollable, on_click=self.on_find)
        find_tile.render()
        self.elements.append(find_tile)

    def _handle_select(self, selected_element):
        """
        Handles the selection of a project tile.
        """
        if self.selected_tile:
            self.selected_tile.set_selected(False)
        self.selected_tile = selected_element
        self.selected_tile.set_selected(True)
        self.on_select(self.selected_tile.data)

    def _add_find_only(self, parent):
        """
        Adds the find-project tile when no projects are available.
        """
        placeholder = FindProjectTileElement(parent, on_click=self.on_find)
        placeholder.render()
        self.elements.append(placeholder)
