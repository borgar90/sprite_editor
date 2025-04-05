import patch_locale
import tkinter as tk
from app.theme import ThemeManager
from app.splash_screen import SplashScreen
from app.project_selector import ProjectSelector
from app.gui_engine import GUIManager
from app.app_logic import AppLogic

SKIP_SPLASH = False  # Sett True for å skipe splash under dev

def launch_gui(root, project_data):
    theme = ThemeManager(root)
    theme.apply_to_root()

    app_logic = AppLogic()

    if project_data["type"] == "new":
        app_logic.create_new_project(project_data["path"], project_data["name"])
    else:
        app_logic.load_project(project_data["path"])

    gui = GUIManager(root, app_logic)

    app_logic.on_preview_refresh = gui.generate_preview

    def on_image_loaded(image):
        gui.display_image(image)
        gui.generate_preview()

    app_logic.on_image_loaded = on_image_loaded

    root.deiconify()  # 👈 Her først vises hovedvinduet
    root.lift()

def on_project_selected(root, project_data):
    if project_data:
        launch_gui(root, project_data)


def after_splash(root):
    # ✅ IKKE deiconify root her!

    def on_project_selected(project_data):
        if project_data:
            launch_gui(root, project_data)  # <- dette skal ha med data

    ProjectSelector(root, on_project_selected)

def main():
    root = tk.Tk()


    if SKIP_SPLASH:
        print("[DEV] Skipping splash screen...")
        after_splash(root)
    else:
        SplashScreen(root, after_splash)

    root.mainloop()

if __name__ == "__main__":
    main()
