import pyautogui
import pyperclip
from pynput.mouse import Listener

def on_click(x, y, button, pressed):
  """Gets the mouse position on click and copies it to the clipboard."""
  if pressed:
    position = (x, y)
    position_str = f"({position[0]}, {position[1]})"
    pyperclip.copy(position_str)
    print(f"Copied mouse position: {position_str}")

# Start the click listener
with Listener(on_click=on_click) as listener:
  listener.join()

chatBar = (2973, 1030)
message = (2997, 955)
copyText = (3057, 753)