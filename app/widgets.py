import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

ICON_CACHE = {}

def load_icon(path, size=(16, 16)):
    """Loads and caches an icon image"""
    if path not in ICON_CACHE:
        img = Image.open(path).resize(size, Image.ANTIALIAS)
        ICON_CACHE[path] = ImageTk.PhotoImage(img)
    return ICON_CACHE[path]

def create_label(parent, text="", icon=None, **kwargs):
    """Creates a styled label, optionally with icon"""
    if icon:
        icon_img = load_icon(icon)
        label = ttk.Label(parent, text=f"  {text}", image=icon_img, compound="left", **kwargs)
        label.image = icon_img  # Keep reference
        return label
    return ttk.Label(parent, text=text, **kwargs)

def create_button(parent, text="", command=None, icon=None, **kwargs):
    """Creates a styled button, optionally with icon"""
    if icon:
        icon_img = load_icon(icon)
        btn = ttk.Button(parent, text=f"  {text}", image=icon_img, compound="left", command=command, **kwargs)
        btn.image = icon_img
        return btn
    return ttk.Button(parent, text=text, command=command, **kwargs)

def create_entry(parent, textvariable=None, **kwargs):
    """Creates a styled entry"""
    return ttk.Entry(parent, textvariable=textvariable, **kwargs)

def create_combobox(parent, values, variable=None, **kwargs):
    """Creates a styled combobox"""
    combo = ttk.Combobox(parent, values=values, textvariable=variable, state="readonly", **kwargs)
    if variable:
        combo.set(variable.get())
    else:
        combo.set(values[0])
    return combo

def create_separator(parent, **kwargs):
    return ttk.Separator(parent, orient="horizontal", **kwargs)
