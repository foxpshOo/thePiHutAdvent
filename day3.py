import time

from machine import Pin


class State:
    def __init__(self):
        self._pressed = False
    
    def button_down(self):
        self._pressed = True

    def button_up(self):
        self._pressed = False

    def is_pressed(self):
        return self._pressed
    

def check_button(pin, state):
    if pin.value() == 1:
        if not(state.is_pressed()):
            state.button_down() 
            return True
            print(f"{pin} button pressed, {t=}")
    else:
        state.button_up()
    return False

redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)
redLED = Pin(14, Pin.OUT)
#greenLED = Pin(25, Pin.OUT)

t = 0.5

print("go banananana")

previous_update = 0

redbutton_state = State()
greenbutton_state = State()

while True: # Loop forever

    if check_button(redbutton, redbutton_state):
        t *= 2
        print(f"red button pressed, {t=}")
    

    if check_button(greenbutton, greenbutton_state):
        t /= 2 
        print(f"green button pressed {t=}")

    now = time.time_ns()
    if now - previous_update > t * 10**9:
        redLED.toggle()
        previous_update = now