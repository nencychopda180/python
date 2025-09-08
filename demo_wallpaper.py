import os
import time
import ctypes
import keyboard
import random

# Path to your wallpaper folder
WALLPAPER_FOLDER = r"d:\hanumanji"  # Change this to your folder path

# Windows function to set wallpaper
def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

# Get all image files in the folder
def get_images(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder)
            if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

def main():
    images = get_images(WALLPAPER_FOLDER)
    if not images:
        print("No images found in the folder.")
        return

    print("Wallpaper changer started. Press 'a' to stop.")
    
    try:
        while True:
            img = random.choice(images)
            set_wallpaper(img)
            print(f"Wallpaper set to: {img}")
            for _ in range(50):  # Check for key press every 0.1s (total 5s)
                if keyboard.is_pressed('a'):
                    print("Stopping wallpaper changer.")
                    return
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("Interrupted by user.")

if __name__ == "__main__":
    main()
