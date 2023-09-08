from machine import Pin
from time import sleep

led1 = Pin(26, Pin.OUT, value=0)
pb1 = Pin(4, Pin.IN)
bananer = 0 
while True:
    
    first = pb1.value()
    sleep(0.01)
    second = pb1.value()
    # Tjekker om knap trykkes
    # hvis knap værdi går fra 1 (True) til 0 (False)
    if first == 1 and second == 0:
        print("Knap trykket")
        if led1.value() == 0:
            led1.on()
        elif led1.value()== 1:
            led1.off()