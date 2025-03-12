from time import sleep
from gpiozero import LED
import app
import time
# Define LEDs
red_1 = LED(10) # 4th pin 
yellow_1 = LED(9) # keela iruthu 5th pin 
green_1 = LED(11) #2nd pin

red_2 = LED(17) # 6th pin from the up side
yellow_2 = LED(27) #7th pin from the up side
green_2 = LED(22) #8th  pin from the up side

def forcheck():
    red_1.on()
    sleep(5)
    red_1.off()
    yellow_1.on()
    sleep(5)
    yellow_1.off()
    green_1.on()
    sleep(5)
    green_1.off()
    red_2.on()
    sleep(5)
    red_2.off()
    yellow_2.on()
    sleep(5)
    yellow_2.off()
    green_2.on()
    sleep(5)
    green_2.off()

forcheck()