import tkinter as tk
from PIL import ImageTk
from app.menu_bar import MenuBar
from tkinter import ttk
from app.tools_panel import ToolsPanel
from app.painter_canvas import PainterCanvas
from app.palette_panel import PalettePanel
from app.left_menu import LeftMenu
from app.right_panel import RightPanel
from tkinter import ttk
from app.file_tabs_manager import FileTabsManager
from app.gui_elements.screen_manager import ScreenManager
from app.gui_elements.palette_popup import PalettePopup
from app.gui_elements.preview_renderer import PreviewRenderer


class GUIManager:
    def __init__(self, root, app_logic):
        self.zoom_level = 1.0
        self.root = root
        self.app_logic = app_logic
        self.on_add_file = self.app_logic.on_add_file

        self.root.title("SpriteToJSON Tool")

        self._create_main_layout()

        style = ttk.Style()
        style.configure("FileBar.TFrame", background="#3a3a3a")
        style.configure("FileLabel.TLabel", background="#3a3a3a", foreground="white", padding=10)
        style.configure("AddButton.TButton", padding=10)

        self._setup_window()
        self._create_menu()
        self.file_tabs = FileTabsManager(self.root, on_close_callback=self._on_file_closed)
        self.file_tabs.set_on_switch_callback(self._on_tab_switched)

        self._create_main_layout()

    def _setup_window(self):
        self.root.geometry("1000x600")
        self.root.minsize(800, 500)

    def _create_menu(self):
        self.menu_bar = MenuBar(self.root, self.app_logic, self.switch_screen)
        self.root.config(menu=self.menu_bar.menu)

    def _create_main_layout(self):
        self.screen_manager = ScreenManager(self.root, self.app_logic, self.mode_label)
        self.paint_container, self.preview_container = self.screen_manager.init_widgets(self.main_frame)

        self.palette_popup = PalettePopup(self.root, self.app_logic, self._on_tile_selected)
        self.preview_renderer = PreviewRenderer(
            self.root, self.app_logic,
            self.preview_canvas, self.grid_container,
            self.grid_window, lambda: self.zoom_level
        )


        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)
        # Top layout container

        self.layout_frame = ttk.Frame(self.main_frame)
        self.layout_frame.pack(fill="both", expand=True)

        # FILE BAR just below menubar
        self._create_working_file_bar(self.layout_frame)

        # Main content below file bar
        self.main_frame = ttk.Frame(self.layout_frame)
        self.main_frame.pack(fill="both", expand=True)


        # LEFT: Toolbar / Menu
        self.left_menu = LeftMenu(
            self.root,
            on_switch_mode=self.switch_screen,
            on_open_palette=self._open_palette_popup
        )

        # LEFT PANEL (Label + Palette)
        self.left_panel = ttk.Frame(self.main_frame, width=180)
        self.left_panel.pack(side="left", fill="y", padx=10, pady=10)

        self.mode_label = ttk.Label(self.left_panel, text="🛠️ Painter Mode", font=("Arial", 12, "bold"))
        self.mode_label.pack(anchor="w", pady=(0, 10))

        # CENTER: Preview container with scrollable canvas
        self.preview_container = ttk.Frame(self.main_frame)
        self._create_scrollable_preview_canvas()

        # PAINT CONTAINER (hidden/shown by mode)
        self.paint_container = ttk.Frame(self.main_frame)

        # Painter canvas setup
        self.painter = PainterCanvas(self.paint_container, self.app_logic)

        # RIGHT PANEL (Tile/Grid Groups)
        self.right_panel_frame = ttk.Frame(self.main_frame, width=200)
        self.right_panel_frame.pack(side="right", fill="y", padx=10, pady=10)

        self.right_panel = RightPanel(self.right_panel_frame, self.app_logic, self.generate_preview)

        # Default screen
        self.switch_screen("paint")

    def get_tool_frame(self):
        return self.tool_frame

    def display_image(self, pil_image):
        self.preview_canvas.delete("all")
        img_copy = pil_image.copy()
        img_copy.thumbnail((512, 512))
        self._tk_image = ImageTk.PhotoImage(img_copy)
        self.preview_canvas.create_image(256, 256, image=self._tk_image)

    def _animate_preview(self):
        if not self._tk_frames:
            return

        self.preview_canvas.delete("all")
        frame = self._tk_frames[self._current_anim_frame]
        self.preview_canvas.create_image(256, 256, image=frame)

        self._current_anim_frame = (self._current_anim_frame + 1) % len(self._tk_frames)
        self.root.after(150, self._animate_preview)

    def _draw_grid_overlay(self, canvas, tile_w, tile_h, cols, rows, image_width, image_height):
        grid_width = min(cols * tile_w, image_width)
        grid_height = min(rows * tile_h, image_height)

        for x in range(0, grid_width + 1, tile_w):
            canvas.create_line(x, 0, x, grid_height, fill="#555")

        for y in range(0, grid_height + 1, tile_h):
            canvas.create_line(0, y, grid_width, y, fill="#555")

    def switch_screen(self, screen_name):
        # Hide both containers first
        self.preview_container.pack_forget()
        self.paint_container.pack_forget()

        # Show the selected screen in the center (between left and right panels)
        if screen_name == "paint":
            self.paint_container.pack(side="left", fill="both", expand=True, padx=10, pady=10)
            self.mode_label.config(text="🛠️ Painter Mode")

        elif screen_name == "preview":
            self.preview_container.pack(side="left", fill="both", expand=True, padx=10, pady=10)
            self.mode_label.config(text="🔍 Preview Mode")

    def _on_tile_selected(self, tile_id, tile_image, layer):
        self.painter.set_selected_tile(tile_id, tile_image, layer)

    def _open_palette_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Palette Editor")
        popup.configure(bg="#1e1e2e")

        # Optional: make it non-resizable or fixed size
        popup.geometry("640x400")
        popup.minsize(400, 300)

        # Center popup
        popup.transient(self.root)
        popup.grab_set()

        # Add PalettePanel inside the popup
        PalettePanel(popup, self.app_logic, self._on_tile_selected)

    def generate_preview(self):
        self.preview_canvas.delete("all")
        for widget in self.grid_container.winfo_children():
            widget.destroy()

        tw, th = self.app_logic.tile_width, self.app_logic.tile_height
        cols, rows = self.app_logic.grid_cols, self.app_logic.grid_rows
        zoom = self.zoom_level

        tile_w = int(tw * zoom)
        tile_h = int(th * zoom)

        img_width = cols * tile_w
        img_height = rows * tile_h

        # --- Resize image if available ---
        if self.app_logic.image:
            img = self.app_logic.image.copy()
            img = img.resize((int(img.width * zoom), int(img.height * zoom)))
            self._tk_image = ImageTk.PhotoImage(img)

            img_label = tk.Label(self.grid_container, image=self._tk_image, bg="#2a2a2a")
            img_label.place(x=0, y=0)

            img_width = img.width
            img_height = img.height

        # --- Set grid container to match image or tile area ---
        self.grid_container.config(width=img_width, height=img_height)
        self.preview_canvas.coords(self.grid_window, 0, 0)
        self.preview_canvas.itemconfig(self.grid_window, width=img_width, height=img_height)

        # --- Draw grid overlay ---
        for x in range(0, img_width + 1, tile_w):
            self.preview_canvas.create_line(x, 0, x, img_height, fill="#555")

        for y in range(0, img_height + 1, tile_h):
            self.preview_canvas.create_line(0, y, img_width, y, fill="#555")

        # --- Update scrollregion ---
        self.preview_canvas.configure(scrollregion=self.preview_canvas.bbox("all"))
        self.preview_canvas.update_idletasks()

    def _create_scrollable_preview_canvas(self):
        # Container frame
        self.scroll_canvas_frame = ttk.Frame(self.preview_container)
        self.scroll_canvas_frame.pack(fill="both", expand=True)

        # Scrollbars
        self.scroll_x = tk.Scrollbar(self.scroll_canvas_frame, orient="horizontal")
        self.scroll_y = tk.Scrollbar(self.scroll_canvas_frame, orient="vertical")

        self.scroll_x.pack(side="bottom", fill="x")
        self.scroll_y.pack(side="right", fill="y")

        # Canvas
        self.preview_canvas = tk.Canvas(
            self.scroll_canvas_frame,
            bg="#2a2a2a",  # darker gray
            xscrollcommand=self.scroll_x.set,
            yscrollcommand=self.scroll_y.set,
            highlightthickness=0
        )
        self.preview_canvas.pack(side="left", fill="both", expand=True)

        self.scroll_x.config(command=self.preview_canvas.xview)
        self.scroll_y.config(command=self.preview_canvas.yview)

        # Container inside canvas for future grid layers
        self.grid_container = tk.Frame(self.preview_canvas, bg="#2a2a2a")
        self.grid_window = self.preview_canvas.create_window(0, 0, anchor="nw", window=self.grid_container)

        # Bind resizing to update scrollregion
        self.grid_container.bind("<Configure>",
                                 lambda e: self.preview_canvas.configure(scrollregion=self.preview_canvas.bbox("all")))

        # Zoom handling
        self.preview_canvas.bind("<MouseWheel>", self._handle_zoom)
        self.zoom_level = 1.0

        # Optional: Scroll with mousewheel
        self.preview_canvas.bind("<Enter>", lambda e: self.preview_canvas.focus_set())
        self.preview_canvas.bind("<MouseWheel>",
                                 lambda e: self.preview_canvas.yview_scroll(-1 * (e.delta // 120), "units"))
        self.preview_canvas.bind("<Shift-MouseWheel>",
                                 lambda e: self.preview_canvas.xview_scroll(-1 * (e.delta // 120), "units"))

    def _handle_zoom(self, event):
        zoom_factor = 1.1 if event.delta > 0 else 0.9
        new_zoom = self.zoom_level * zoom_factor
        if 0.2 <= new_zoom <= 5:
            self.zoom_level = new_zoom
            self.generate_preview()


    def _create_working_file_bar(self, parent):
        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(side="top", fill="x")

        # Load existing project files here (if any)
        self.open_tabs = []

        self._add_new_file_tab_button()

        # Container frame for working files
        file_bar_container = ttk.Frame(parent, style="FileBar.TFrame")
        file_bar_container.pack(side="top", fill="x")

        # Scrollable canvas
        self.file_canvas = tk.Canvas(file_bar_container, height=40, bg="#3a3a3a", highlightthickness=0)
        self.file_canvas.pack(side="left", fill="both", expand=True)

        self.scroll_frame = ttk.Frame(self.file_canvas, style="FileBar.TFrame")
        self.scroll_window = self.file_canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        # Add scrollbar (hidden by default)
        self.file_scrollbar = ttk.Scrollbar(file_bar_container, orient="horizontal", command=self.file_canvas.xview)
        self.file_canvas.configure(xscrollcommand=self.file_scrollbar.set)

        # Bind scroll visibility on hover
        self.file_canvas.bind("<Enter>", lambda e: self.file_scrollbar.pack(side="bottom", fill="x"))
        self.file_canvas.bind("<Leave>", lambda e: self.file_scrollbar.pack_forget())

        # Populate with example files
        for i in range(1, 12):
            ttk.Label(self.scroll_frame, text=f"file_{i}.stj", style="FileLabel.TLabel").pack(side="left", padx=(6, 0))

        # + Add new button
        ttk.Button(self.scroll_frame, text="+", style="AddButton.TButton", command=self.on_add_file).pack(side="left", padx=10)

        # Update scrollregion
        self.scroll_frame.bind("<Configure>", lambda e: self.file_canvas.configure(scrollregion=self.file_canvas.bbox("all")))

    def _add_new_file_tab_button(self):
        plus_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(plus_tab, text="+")
        self.tab_control.bind("<<NotebookTabChanged>>", self._on_tab_changed)

    def _on_tab_changed(self, event):
        selected_index = self.tab_control.index("current")
        if selected_index == self.tab_control.index("end") - 1:  # "+" tab clicked
            self._create_new_file_tab()

    def _create_new_file_tab(self, filename=None):
        import uuid
        file_id = filename if filename else f"untitled_{uuid.uuid4().hex[:4]}.stj"
        new_tab = ttk.Frame(self.tab_control)
        self.tab_control.insert("end-1", new_tab, text=file_id)  # Insert before "+"
        self.open_tabs.append((file_id, new_tab))
        self.tab_control.select(new_tab)

        # TODO: you could load actual canvas/tools into new_tab here

    def _on_file_closed(self, filename):
        file_data = self.file_tabs.tabs.get(filename)
        if file_data:
            # TODO: Check unsaved changes via Interceptor before removing
            tab = file_data["frame"]
            self.file_tabs.notebook.forget(tab)
            del self.file_tabs.tabs[filename]

    def _on_tab_switched(self, filename):
        print(f"[GUI] Switched to file: {filename}")
        # TODO: update right panel, tool settings, canvas etc.
