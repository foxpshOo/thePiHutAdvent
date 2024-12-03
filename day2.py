import time

from machine import Pin

redLED = Pin(14, Pin.OUT)
greenLED = Pin(25, Pin.OUT)

def glow(led, is_long):
    t = 1.5 if is_long else 0.5
    led.value(1)
    time.sleep(t)
    led.value(0)
    time.sleep(0.1)

while True:
    glow(redLED, is_long=True)
    glow(greenLED, is_long=True)
    for i in range(3):
        glow(greenLED, is_long=False)
