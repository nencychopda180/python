import keyboard

def on_key(event):
    print(f"Key pressed: {event.name}")

keyboard.on_press(on_key)
keyboard.wait()
