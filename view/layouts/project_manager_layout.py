import tkinter as tk
from PIL import ImageTk
from view.layouts.base_layout import BaseLayout
from view.sections.project_list_section import ProjectListSection
from view.sections.create_button_section import CreateButtonSection

class ProjectManagerLayout(BaseLayout):
    """
    Layout that composes all UI sections for the core editing screen.
    Organizes menu, bar, canvas, tools, and right-side panel.
    """
    def __init__(self, root):
        BaseLayout.__init__(self, root)
        self.root = root
        self.project_data = root.app_context.projects
        self.select_project = root.select_project
        self.create_project = root.create_project
        self.find_project = root.find_project
        self.logo = root.app_context.logo
        self.sections = []  # Store the sections in the layout
        self.create()

    def create(self):
        """
        Create all the sections for the layout.
        """
        # Create project list section
        list_section = ProjectListSection(
            name="ProjectList",
            project_data=self.project_data,
            on_select=self.select_project,
            on_find=self.find_project
        )

        # Create create project button section
        create_section = CreateButtonSection(
            name="CreateButton",
            on_create=self.create_project
        )

        # Add sections to the layout
        self.add_section(list_section)
        self.add_section(create_section)

    def render(self):
        """
        Renders the layout, including the frame, canvas, and sections.
        """
        # Create the main frame for the layout
        self.frame = tk.Frame(self.root, bg="white", bd=2, relief="solid")
        self.frame.pack(fill="both", expand=True)

        # Create the canvas that will hold the scrollable area
        canvas = tk.Canvas(self.frame, bg="#1e1e1e", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=canvas.yview)
        scrollable = tk.Frame(canvas, bg="#1e1e1e")

        # Bind the scrolling area to adjust the scroll region
        scrollable.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a window in the canvas to hold the scrollable frame
        canvas.create_window((0, 0), window=scrollable, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack the canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Render the logo (this could be a label or any element)
        logo_label = tk.Label(canvas, image=self.logo, bg="white")
        logo_label.pack(pady=10)

        # Render all sections in the scrollable frame
        for section in self.sections:
            section.render(scrollable)

    def add_section(self, section):
        """
        Add a section to the layout.
        """
        self.sections.append(section)
