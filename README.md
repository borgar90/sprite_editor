# 🧪 SpriteToJSON

![Status](https://img.shields.io/badge/status-in_development-orange)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macOS-blue)
![Python](https://img.shields.io/badge/python-3.12%2B-green)


**SpriteToJSON** is a powerful, modern visual toolkit for game developers, pixel artists, and technical designers to slice, preview, organize and export sprite sheets or tilemaps with ease — visually and efficiently.

---

## 🧠 What Is This?

SpriteToJSON is a **standalone desktop tool** written in Python + Tkinter, designed to solve the pain of managing and exporting sprite sheet metadata. It brings a modern UI experience to a problem most developers handle manually or with outdated tools.

---

## 🎯 The Problem It Solves

💀 Manually editing JSON or `.tmx` tile definitions
😫 Slicing sprites by guessing offset and tile size
🛠️ Rewriting animations frame by frame in your engine

### SpriteToJSON gives you:

✅ Drag & drop tile slicing
✅ Frame-by-frame animation preview
✅ Tiled `.json` and custom `.json` export
✅ Zoomable, scrollable grid with visual feedback
✅ Project management for multiple sprite sets
✅ Support for image previews, tile locking, and more

---

## ✨ Features

| Feature                        | Status     |
|-------------------------------|------------|
| 🔥 Splash screen animation     | ✅ Done     |
| 🗂️ Project system (`.stjproj`) | ✅ Done     |
| 🎛️ UI with dark mode          | ✅ Done     |
| 📐 Grid + zoomable canvas      | ✅ Done     |
| 🎨 Painter mode (preview)      | 🧪 In Dev   |
| 🧩 Drag tile resizer tool      | 🔜 Planned  |
| 🎞️ Animation timeline          | 🔜 Planned  |
| 💾 JSON / Tiled export         | 🧪 Partial  |
| 🤖 AI frame tagging (future)   | 🧪 Research |

---

## 🚀 Quickstart

```bash
git clone https://github.com/yourusername/SpriteToJSON.git
cd SpriteToJSON
python -m venv .venv
.venv\Scripts\activate   # or source .venv/bin/activate on macOS/Linux
pip install -r requirements.txt
python main.py


🛠 Tech Stack
Python 3.12+

tkinter + ttkbootstrap

Pillow (PIL) for image rendering

Custom ProjectManager + .stjproj format

JSON-based export

📁 Folder Structure
assets/
├── splash/                # Character animations + logo
app/
├── splash_screen.py       # Launch animation
├── project_selector.py    # Project UI
├── gui_engine.py          # App shell and layout
├── right_panel.py         # Tile/grid inputs
core/
├── exporter.py            # Export logic for JSON/Tiled

🧪 Development Status
SpriteToJSON is in active prototyping phase. Most UI components are implemented, including:

Splash screen with animated sprite + fading logo

Fully themed UI (dark mode)

Collapsible side panels

Grid preview

Basic project creation + loading logic

Next milestones:

Frame timeline support

Tile-based drawing and tagging

Tiled-compatible .json and .tmx export

🔮 Vision
We’re building SpriteToJSON to become the go-to visual companion for indie devs working with sprites, tiles, and frame-by-frame animations — whether for game engines, web projects, or prototyping tools.

The goal is to eliminate the need for manual metadata creation and allow artists to focus on creativity, not format specs.

👤 Author
Created by Borgar Flaen Stensrud
Splash character, sprite logic and code brewed with ☕ and 💾
Logo & mascot powered by pixel-art and good taste