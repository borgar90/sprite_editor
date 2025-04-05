import json
import os
from PIL import Image

# --- Atlas Exporter ---

def export_atlas_json(output_path, image_path, tile_width, tile_height, slice_start, slice_end):
    img = Image.open(image_path)
    w, h = img.size

    frames = {}
    idx = 0
    for y in range(0, h, tile_height):
        for x in range(0, w, tile_width):
            if slice_start <= idx <= slice_end:
                frames[f"tile_{idx}"] = {
                    "frame": {"x": x, "y": y, "w": tile_width, "h": tile_height}
                }
            idx += 1

    atlas_data = {
        "frames": frames,
        "meta": {
            "image": os.path.basename(image_path),
            "tile_width": tile_width,
            "tile_height": tile_height,
            "scale": 1
        }
    }

    with open(output_path, 'w') as f:
        json.dump(atlas_data, f, indent=4)

    print(f"[exporter] Atlas JSON exported to {output_path}")

# --- TiledMap Exporter ---

def export_tiledmap_json(output_path, image_path, tile_width, tile_height):
    img = Image.open(image_path)
    w, h = img.size
    cols = w // tile_width
    rows = h // tile_height

    tiled_data = {
        "height": rows,
        "width": cols,
        "tilewidth": tile_width,
        "tileheight": tile_height,
        "orientation": "orthogonal",
        "renderorder": "right-down",
        "version": "1.2",
        "tiledversion": "1.9.2",
        "type": "map",
        "tilesets": [
            {
                "firstgid": 1,
                "columns": cols,
                "image": os.path.basename(image_path),
                "imageheight": h,
                "imagewidth": w,
                "margin": 0,
                "name": "tileset",
                "spacing": 0,
                "tilecount": cols * rows,
                "tileheight": tile_height,
                "tilewidth": tile_width,
                "type": "tileset",
                "version": "1.2"
            }
        ],
        "layers": [
            {
                "type": "tilelayer",
                "name": "ground",
                "width": cols,
                "height": rows,
                "opacity": 1,
                "visible": True,
                "x": 0,
                "y": 0,
                "data": [1] * (cols * rows)
            }
        ]
    }

    with open(output_path, 'w') as f:
        json.dump(tiled_data, f, indent=4)

    print(f"[exporter] TiledMap JSON exported to {output_path}")
