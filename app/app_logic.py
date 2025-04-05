from PIL import Image
import os
from core.exporter import export_atlas_json, export_tiledmap_json
import json
from datetime import datetime

class AppLogic:
    def __init__(self):
        # --- Persistent State ---
        self.image_path = None
        self.image = None
        self.tile_width = 32
        self.tile_height = 32
        self.slice_start = 0
        self.slice_end = 1000
        self.mode = "atlas"  # or "tiledmap"
        self.current_layer = "base"
        self.grid_cols = 16  # eller hent fra brukerinput
        self.grid_rows = 16

        # --- Callbacks ---
        self.on_image_loaded = None
        self.on_preview_refresh = None
        self.on_json_export = None
        self.tool_mode = ""

    # --- Logic Actions ---

    def load_image(self, path):
        if os.path.exists(path):
            self.image_path = path
            self.image = Image.open(path)
            if self.on_image_loaded:
                self.on_image_loaded(self.image)
            print(f"[AppLogic] Image loaded: {path}")


    def export_json(self, export_path):
        if not self.image:
            print("[AppLogic] No image loaded.")
            return



        if self.mode == "atlas":
            export_atlas_json(
                export_path,
                self.image_path,
                self.tile_width,
                self.tile_height,
                self.slice_start,
                self.slice_end
            )
        else:
            export_tiledmap_json(
                export_path,
                self.image_path,
                self.tile_width,
                self.tile_height
            )

        if self.on_json_export:
            self.on_json_export()
        print(f"[AppLogic] Exported JSON to: {export_path}")

    def request_preview(self):
        if self.on_preview_refresh:
            self.on_preview_refresh()

    def load_project_data(self, data):
        self.project_path = data["path"]
        self.is_new_project = data["type"] == "new"
        print(f"[AppLogic] Loaded project: {self.project_path} (new: {self.is_new_project})")


    def create_new_project(self, base_path, name=None):
        if not name:
            name = f"Project_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        self.project_path = os.path.join(base_path, name)
        self.project_name = name
        os.makedirs(self.project_path, exist_ok=True)

        # Subdirectories
        os.makedirs(os.path.join(self.project_path, "images"), exist_ok=True)
        os.makedirs(os.path.join(self.project_path, "maps"), exist_ok=True)
        os.makedirs(os.path.join(self.project_path, "config"), exist_ok=True)

        # Save project file
        self.project_config_file = os.path.join(self.project_path, f"{name}.stjproj")
        config = {"name": name, "created": datetime.now().isoformat()}
        with open(self.project_config_file, "w") as f:
            json.dump(config, f)

        print(f"🆕 Created new project at: {self.project_path}")


    def open_project(self):
        print("📂 Open project triggered")

    def save_project(self):
        print("💾 Save project triggered")

    def close_project(self):
        print("❌ Close project triggered")

