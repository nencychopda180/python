import ctypes
import os

def set_wallpaper(image_path):
    # Convert relative path to absolute path
    abs_path = os.path.abspath(image_path)
    # Change wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)

# Example usage
set_wallpaper(r"D:\hanumanji\IMG-20250714-WA0178.jpg")