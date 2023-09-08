from machine import Pin
from time import sleep

pb1 = Pin(4, Pin.IN)

while True:
 print("Knap vaerdi: ", pb1.value())
 sleep(0.1)