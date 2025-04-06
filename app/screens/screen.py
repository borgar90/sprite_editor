from app.layout.layout import Layout

class Screen:
    def __init__(self, root, app_logic=None):
        super().__init__(root, app_logic)
        self.layout = Layout(root, app_logic)

    def add_layout(self, layout):
        self.layout = layout

    def render(self):
        self.layout.render()
