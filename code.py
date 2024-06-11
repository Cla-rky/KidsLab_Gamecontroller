import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Set up the keyboard
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Define the buttons and their corresponding keys

"""
Hier kannst du deine eigenen Keycodes definieren - Was für Tasten brauchst du für dein Spiel.
Beachte auch, dass du die richtigen Pins (Beispiel: board.GPXX) richtig definierst.
"""

buttons = [
    {"pin": board.GP12, "keycode": Keycode.W},
    {"pin": board.GP13, "keycode": Keycode.A},
    {"pin": board.GP14, "keycode": Keycode.S},
    {"pin": board.GP15, "keycode": Keycode.D},
]

# Set up the buttons as inputs with pull-up resistors
for button in buttons:
    button["input"] = digitalio.DigitalInOut(button["pin"])
    button["input"].direction = digitalio.Direction.INPUT
    button["input"].pull = digitalio.Pull.UP

while True:
    # Check the state of each button
    for button in buttons:
        if not button["input"].value:
            # Button is pressed, send the key press
            keyboard.press(button["keycode"])
            while not button["input"].value:
                # Wait for the button to be released
                pass
            keyboard.release_all()
    time.sleep(0.01)
