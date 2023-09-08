from machine import Pin #henter Machine modul
from time import sleep #henter time modul

RED_PIN=26 # Deklarere variabel RED_PIN og sætter værdien til 26
led1 = Pin(RED_PIN, Pin.OUT) #Kalder Pin funktion og sætter værdierne 

YELLOW_PIN=12 
led2 = Pin(YELLOW_PIN, Pin.OUT)
led2.on() #Giver led2 besked på at slukke

GREEN_PIN=13
led3 = Pin(GREEN_PIN, Pin.OUT)

while True: #starter While loop indtil den er Falsk
        
        print("Red led ON!") #printer til "console"/shell
        led1.on() #tænd
        print("YELLOW led ON!")
        led2.off()  #tænd
        print("GREEN led1 ON!")
        led3.on()  #tænd
        sleep(1)  #pause i 1 sek.
        print("Red led OFF!")
        led1.off() #sluk
        print("YELLOW led OFF!")
        led2.on() #sluk
        print("GREEN led OFF!")
        led3.off() #sluk
        sleep(1) #pause i 1 sek.


