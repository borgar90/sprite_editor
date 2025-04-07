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
        Renders the layout, including the frame, canvas, and sections, with modern styling.
        """
        # Create the main frame for the layout
        self.frame = tk.Frame(self.root, bg="#1e1e2e", bd=2, relief="solid")  # Dark background
        self.frame.pack(fill="both", expand=True)

        # Render the logo at the top
        logo_label = tk.Label(self.frame, image=self.logo, bg="#1e1e2e")
        logo_label.pack(pady=10)

        # Create a frame for the buttons section
        button_frame = tk.Frame(self.frame, bg="#1e1e2e")
        button_frame.pack(pady=(10, 20))

        # Add a "Find Existing Project" button next to the "Create New Project" button
        find_button = tk.Button(
            button_frame,
            text="Find Existing Project",
            font=("Arial", 14, "bold"),
            bg="#ff8800",  # Orange background
            fg="#ffffff",  # White text
            activebackground="#ff9900",  # Slightly lighter orange on hover
            activeforeground="#ffffff",
            relief="raised",
            height=2,
            width=25,
            command=self.find_project
        )
        find_button.pack(side="left", padx=10)

        create_button = tk.Button(
            button_frame,
            text="Create New Project",
            font=("Arial", 14, "bold"),
            bg="#ff8800",  # Orange background
            fg="#ffffff",  # White text
            activebackground="#ff9900",  # Slightly lighter orange on hover
            activeforeground="#ffffff",
            relief="raised",
            height=2,
            width=25,
            command=self.create_project
        )
        create_button.pack(side="left", padx=10)

        # Adjust the "Known Projects" label to remove unnecessary padding
        known_projects_label = tk.Label(
            self.frame,
            text="Known Projects",
            font=("Arial", 16, "bold"),
            bg="#1e1e2e",
            fg="#ffffff",
            anchor="w"
        )
        known_projects_label.pack(fill="x", padx=20, pady=(5, 0))  # Reduce bottom padding

        # Create a frame for the project grid section right after the "Known Projects" label
        project_grid_frame = tk.Frame(self.frame, bg="#2e2e2e")
        project_grid_frame.pack(fill="x", padx=20, pady=(5, 0))  # Ensure it follows the label

        # Render the project grid with selection functionality
        for index, project in enumerate(self.project_data):
            project_cell = tk.Frame(
                project_grid_frame,
                bg="#2e2e2e",  # Slightly lighter dark tone
                highlightbackground="#2e2e2e",  # Default border color
                highlightthickness=2,
                width=120,
                height=120
            )
            project_cell.grid(row=index // 5, column=index % 5, padx=10, pady=10)  # Place projects in a grid

            # Add an icon above the label (placeholder for now)
            icon_label = tk.Label(
                project_cell,
                text="📁",  # Placeholder icon
                bg="#2e2e2e",
                fg="#ffffff",
                font=("Arial", 24)
            )
            icon_label.pack(pady=(10, 5))

            # Add the project name label
            project_label = tk.Label(
                project_cell,
                text=project["name"],
                bg="#2e2e2e",
                fg="#ffffff",
                font=("Arial", 12)
            )
            project_label.pack()

            # Add click functionality to select the project
            project_cell.bind("<Button-1>", lambda e, p=project, pc=project_cell: self._select_project(p, pc))

    def add_section(self, section):
        """
        Add a section to the layout.
        """
        self.sections.append(section)

    def _select_project(self, project, project_cell):
        """
        Handle project selection and update the UI to reflect the selected project.
        """
        # Reset borders for all project cells
        for widget in project_cell.master.winfo_children():
            widget.configure(highlightbackground="#2e2e2e")

        # Highlight the selected project cell
        project_cell.configure(highlightbackground="#ff8800")

        # Update the selected project in the app context
        self.select_project(project)
