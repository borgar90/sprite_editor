from app.gui_elements.gui_element import GUIElement

class Layout(GUIElement):
    def __init__(self, root, app_logic=None):
        super().__init__(root, app_logic)
        self.elements = []

    def add_element(self, element, position="center"):
        self.elements.append((element, position))

    def render(self):
        for element, position in self.elements:
            if position == "top":
                element.pack(side="top", fill="x")
            elif position == "left":
                element.pack(side="left", fill="y")
            elif position == "right":
                element.pack(side="right", fill="y")
            elif position == "bottom":
                element.pack(side="bottom", fill="x")
            else:
                element.pack(fill="both", expand=True)
