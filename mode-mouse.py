# from pynput.mouse import Controller
# import time

################## MOVE THE MOUSE TO A SPECIFIC LOCATION  ############
# # Create a Controller object to control the mouse
# mouse = Controller()

# # Function to move the mouse smoothly
# def smooth_move(x, y, duration):
#     start_x, start_y = mouse.position
#     step_count = 100  # Number of steps for the movement
#     step_duration = duration / step_count  # Duration of each step

#     delta_x = (x - start_x) / step_count
#     delta_y = (y - start_y) / step_count

#     for _ in range(step_count):
#         mouse.move(delta_x, delta_y)
#         time.sleep(step_duration)

# # Move the mouse in a smooth square pattern
# def move_mouse_smoothly():
#     start_position = mouse.position
#     print(f"Starting position: {start_position}")

#     # Define the distance for each movement
#     distance = 200  # Pixels

#     # Move right
#     smooth_move(start_position[0] + distance, start_position[1], 1)

#     # Move down
#     smooth_move(start_position[0] + distance, start_position[1] + distance, 1)

#     # Move left
#     smooth_move(start_position[0], start_position[1] + distance, 1)

#     # Move up
#     smooth_move(start_position[0], start_position[1], 1)

#     # Return to start
#     print(f"Returned to starting position: {mouse.position}")













from pynput import keyboard, mouse

# Create Controller objects to control the mouse
mouse_controller = mouse.Controller()

# Define the step size for each key press
step_size = 5

# Function to move the mouse based on the key pressed
def on_press(key):
    try:
        if key == keyboard.Key.up:
            # Move the mouse up
            mouse_controller.move(0, -step_size)
        elif key == keyboard.Key.down:
            # Move the mouse down
            mouse_controller.move(0, step_size)
        elif key == keyboard.Key.left:
            # Move the mouse left
            mouse_controller.move(-step_size, 0)
        elif key == keyboard.Key.right:
            # Move the mouse right
            mouse_controller.move(step_size, 0)
    except Exception as e:
        print(f"Error: {e}")

# Start listening for key presses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
