import tkinter as tk
from PIL import ImageTk
from app.menu_bar import MenuBar
from tkinter import ttk
from app.tools_panel import ToolsPanel
from app.painter_canvas import PainterCanvas
from app.palette_panel import PalettePanel
from app.left_menu import LeftMenu
from app.right_panel import RightPanel


class GUIManager:
    def __init__(self, root, app_logic):
        self.zoom_level = 1.0
        self.root = root
        self.app_logic = app_logic
        self.root.title("SpriteToJSON Tool")

        self._setup_window()
        self._create_menu()
        self._create_main_layout()

    def _setup_window(self):
        self.root.geometry("1000x600")
        self.root.minsize(800, 500)

    def _create_menu(self):
        self.menu_bar = MenuBar(self.root, self.app_logic, self.switch_screen)
        self.root.config(menu=self.menu_bar.menu)

    def _create_main_layout(self):
        self.main_frame = ttk.Frame(self.root)
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


