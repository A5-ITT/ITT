from machine import Pin
from time import sleep

RED_PIN=26
led1 = Pin(RED_PIN, Pin.OUT)

# YELLOW_PIN=12
# led2 = Pin(YELLOW_PIN, Pin.OUT)
# led2.on()
# 
# GREEN_PIN=13
# led3 = Pin(GREEN_PIN, Pin.OUT)

while True:
        
        print("Red led ON!")
        led1.on()
        sleep(0.5)
        print("Red led OFF!")
        led1.off()
        sleep(0.5)
#         print("YELLOW led ON!")
#         led2.off()
#         print("GREEN led1 ON!")
#         led3.on()
#         sleep(0.01)
#         print("Red led OFF!")
#         led1.off()
#         print("YELLOW led OFF!")
#         led2.on()
#         print("GREEN led OFF!")
#         led3.off()
# 
