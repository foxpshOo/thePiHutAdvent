import time

from machine import Pin
onboardLED = Pin(25, Pin.OUT)

alph = { "a" : [0,1],
         "b" : [1,0,0,0],
         "c" : [1,0,1,0],
         "d" : [1,0,0],
         "e" : [0],
         "f" : [0,0,1,0],
         "g" : [1,1,0],
         "h" : [0,0,0,0],
         "i" : [0,0],
         "j" : [0,1,1,1],
         "k" : [1,0,1],
         "l" : [0,1,0,0],
         "m" : [1,1],
         "n" : [1,0],
         "o" : [1,1,1],
         "p" : [0,1,1,0],
         "q" : [1,1,0,1],
         "r" : [0,1,0],
         "s" : [0,0,0],
         "t" : [1],
         "u" : [0,0,1],
         "v" : [0,0,0,1],
         "w" : [0,1,1],
         "x" : [1,0,0,1],
         "y" : [1,0,1,1],
         "z" : [1,1,0,0]
    }

def glow (is_short) :
    t = 1.5 if is_short else 0.5
    onboardLED.value(1)
    time.sleep(t)
    onboardLED.value(0)
    time.sleep(0.1)
    

s= "sos"
#s = input()
for c in s :
    for i in alph[c]:
        glow(i)
    time.sleep(0.5)

