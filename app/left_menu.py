import ttkbootstrap as tb
from tkfontawesome import icon_to_image
import tkinter as tk


class LeftMenu:
    def __init__(self, parent, on_switch_mode, on_open_palette):
        screen_width = parent.winfo_screenwidth()
        margin_left = int(screen_width * 0.01)

        self.frame = tb.Frame(parent, bootstyle="dark", width=48)
        self.frame.place(x=margin_left, y=40)
        self.frame.lift()

        self.on_switch_mode = on_switch_mode
        self.on_open_palette = on_open_palette

        self.icons = {}
        self.active_button = None
        self.button_styles = {}
        self.tooltip = None
        self.tooltip_label = None

        self._load_icons()
        self._build_buttons()
        self._add_top_glow()
        self._add_shadow()

    def _load_icons(self):
        self.icons["palette"] = icon_to_image("fill-drip", scale_to_width=20)
        self.icons["paint"] = icon_to_image("paint-brush", scale_to_width=20)
        self.icons["preview"] = icon_to_image("eye", scale_to_width=20)
        # Additional tools for the LeftMenu
        self.icons["zoom"] = icon_to_image("search-plus", scale_to_width=20)
        self.icons["tile_select"] = icon_to_image("border-all", scale_to_width=20)
        self.icons["resize_tool"] = icon_to_image("expand-arrows-alt", scale_to_width=20)

    def _build_buttons(self):
        self.buttons = {}

        # Button label tooltips
        tooltips = {
            "palette": "Palette Picker",
            "paint": "Painter Mode",
            "preview": "Preview Mode",
            "zoom": "Zoom Mode",
            "tile_select": "Select Tooltip",
            "resize_tool": "Resize Tooltip",
        }

        self.buttons["tile_select"] = self._create_icon_button("tile_select", self._activate_tile_select,
                                                               tooltips["tile_select"])
        self.buttons["resize_tool"] = self._create_icon_button("resize_tool", self._activate_resize_tool,
                                                               tooltips["resize_tool"])
        self.buttons["palette"] = self._create_icon_button("palette", self.on_open_palette, tooltips["palette"])

        self.buttons["zoom"] = self._create_icon_button("zoom", self._activate_zoom_tool, tooltips["zoom"])

        self.buttons["paint"] = self._create_icon_button("paint", self.on_switch_mode, tooltips["paint"])
        self.buttons["preview"] = self._create_icon_button("preview", self.on_switch_mode, tooltips["preview"])




        first = True
        for btn in self.buttons.values():
            btn.pack(pady=(12, 0) if first else (0, 0))
            first = False

        self._highlight("paint")

    def _create_icon_button(self, key, command, tooltip_text):
        btn = tb.Button(
            self.frame,
            image=self.icons[key],
            command=command,
            bootstyle="dark-outline",
            width=40
        )
        btn.image = self.icons[key]

        # Store original bootstyle
        self.button_styles[btn] = "dark-outline"

        # Tooltip + hover glow
        btn.bind("<Enter>", lambda e: self._show_tooltip(e, tooltip_text, btn))
        btn.bind("<Leave>", lambda e: self._hide_tooltip())
        btn.bind("<Enter>", lambda e: self._hover_glow(btn), add='+')

        return btn

    def _hover_glow(self, btn):
        original = self.button_styles.get(btn, "dark-outline")
        btn.config(bootstyle="info-outline")
        self.frame.after(180, lambda: btn.config(bootstyle=original))

    def _show_tooltip(self, event, text, widget):
        if self.tooltip_label:
            self.tooltip_label.destroy()

        x = widget.winfo_rootx() + widget.winfo_width() + 10
        y = widget.winfo_rooty() + widget.winfo_height() // 2

        self.tooltip_label = tk.Toplevel(widget)
        self.tooltip_label.overrideredirect(True)
        self.tooltip_label.geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip_label, text=text, bg="#222", fg="white", padx=6, pady=2, font=("Segoe UI", 9))
        label.pack()

    def _hide_tooltip(self):
        if self.tooltip_label:
            self.tooltip_label.destroy()
            self.tooltip_label = None

    def _highlight(self, name):
        for key, btn in self.buttons.items():
            if key == name:
                btn.config(bootstyle="success")
            else:
                btn.config(bootstyle="dark-outline")

    def _switch_mode(self, mode):
        self._highlight(mode)
        self.on_switch_mode(mode)

    def _add_top_glow(self):
        glow = tb.Frame(self.frame, bootstyle="info", height=4)
        glow.pack(fill="x", side="top")

    def _add_shadow(self):
        tb.Frame(self.frame, bootstyle="dark", height=3).pack(fill="x", side="bottom")
        tb.Frame(self.frame, bootstyle="secondary", height=3).pack(fill="x", side="bottom")
        tb.Frame(self.frame, bootstyle="secondary", height=4).pack(fill="x", side="bottom")

    def _activate_zoom_tool(self):
        self._highlight("zoom")


    def _activate_tile_select(self):
        self._highlight("tile_select")


    def _activate_resize_tool(self):
        self._highlight("resize_tool")

