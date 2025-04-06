import os
import json
from PIL import Image, ImageTk


class INITApp:
    def __init__(self, app_context):
        self.app_context = app_context
        self.app_context.projects = []
        self.projects_data_path = "projects.json"
        self.set_logo()
        self.load_projects_from_json()

    def set_logo(self):
        # Load the logo for the app
        logo_img_raw = Image.open("assets/splash/sprite_logo.png").convert("RGBA").resize((400, 120))
        logo_img_tk = ImageTk.PhotoImage(logo_img_raw)
        self.app_context.logo = logo_img_tk

    def load_projects_from_json(self):
        """Load projects from the JSON file and validate paths."""
        if os.path.exists(self.projects_data_path):
            with open(self.projects_data_path, 'r') as file:
                try:
                    data = json.load(file)
                    projects = data.get("projects", [])
                    self.app_context.projects = []
                    for project in projects:
                        name = project.get("name")
                        path = project.get("path")
                        if self.is_valid_project_path(path):
                            self.app_context.projects.append({"name": name, "path": path})
                            print(f"Loaded project: {name}")
                        else:
                            print(f"Invalid project path: {path}")
                except json.JSONDecodeError:
                    print(f"Error loading {self.projects_data_path}: Invalid JSON format.")
        else:
            print(f"JSON file {self.projects_data_path} not found. Starting with no projects.")

    def is_valid_project_path(self, path):
        """Check if the project path exists and is a valid project."""
        return os.path.exists(path) and path.endswith(".stjproj")

    def save_projects_to_json(self):
        """Save the projects to the JSON file."""
        projects = [{"name": project["name"], "path": project["path"]} for project in self.app_context.projects]
        with open(self.projects_data_path, 'w') as file:
            json.dump({"projects": projects}, file, indent=4)
        print(f"Projects saved to {self.projects_data_path}")

    def add_project(self, name, path):
        """
        Adds a new project to the list of projects and saves it to the JSON file.

        :param name: The name of the project
        :param path: The path to the project .stjproj file
        """
        if not self.is_valid_project_path(path):
            print(f"Invalid project path: {path}")
            return

        # Add the new project to the app_context
        new_project = {"name": name, "path": path}
        self.app_context.projects.append(new_project)

        # Save the updated project list to JSON
        self.save_projects_to_json()

        print(f"New project added: {name}")
