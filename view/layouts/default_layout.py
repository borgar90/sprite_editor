# view/layouts/default_layout.py
from view.layouts.layout import Layout
from view.sections.left_panel_section import LeftPanelSection
from view.sections.right_panel_section import RightPanelSection
from view.sections.canvas_section import CanvasSection

class DefaultLayout(Layout):
    def __init__(self, parent, app_logic, on_switch_mode, on_open_palette, on_grid_updated):
        super().__init__(parent)
        self.left = LeftPanelSection(self.parent, app_logic, on_switch_mode, on_open_palette)
        self.center = CanvasSection(self.parent, app_logic)
        self.right = RightPanelSection(self.parent, app_logic, on_grid_updated)

    def render(self):
        self.add_section(self.left, side="left", fill="y", padx=10, pady=10)
        self.add_section(self.center, side="left", fill="both", expand=True, padx=10, pady=10)
        self.add_section(self.right, side="right", fill="y", padx=10, pady=10)
