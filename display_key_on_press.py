from pynput import keyboard

def on_press(key):
    try:
        print(f'Key {key.char} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when escape key is pressed
        return False

# Start the listener
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
