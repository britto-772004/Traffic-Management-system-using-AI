from time import sleep
from gpiozero import LED
import app
import time
# Define LEDs
red_1 = LED(4) # 4th pin 
yellow_1 = LED(6) # keela iruthu 5th pin 
green_1 = LED(2) #2nd pin

red_2 = LED(17) # 6th pin from the up side
yellow_2 = LED(27) #7th pin from the up side
green_2 = LED(22) #8th  pin from the up side

# def light():
#     try:
#         while True:
#             # Red Light ON
#             red.on()
#             yellow.off()
#             green.off()
#             print("Red Light ON")
#             sleep(5)  # Wait 5 seconds

#             # Yellow Light ON
#             red.off()
#             yellow.on()
#             green.off()
#             print("Yellow Light ON")
#             sleep(5)  # Wait 2 seconds

#             # Green Light ON
#             red.off()
#             yellow.off()
#             green.on()
#             print("Green Light ON")
#             sleep(5)  # Wait 5 seconds

#     except KeyboardInterrupt:
#         print("Exiting... Cleaning up GPIO")
#         red.off()
#         green.off() 


def funtime():
    result = app.greentime()
    print("return value from the greentime function : ", result)
    ans = result["number"]
    print("Green time :",ans)
    return ans

while True:
    red_1.on()
    print("Red light is on....")
    sleep(5)
    red_1.off()
    print("Red light is off....")
    yellow_1.on()
    print("yellow light is on....")
    ans=funtime()
    # sleep(3)
    sleep(1)
    yellow_1.off()
    print("yellow light is off....")
    # ans=time()
    green_1.on()
    print("Green light is on....")
    sleep(ans-25)
    green_1.off()
    print("Green light is off....")

    red_2.on()
    print("Red light is on....")
    sleep(5)
    red_2.off()
    print("Red light is off....")
    yellow_2.on()
    print("yellow light is on....")
    ans=funtime()
    # sleep(3)
    sleep(1)
    yellow_2.off()
    print("yellow light is off....")
    # ans=time()
    green_2.on()
    print("Green light is on....")
    sleep(ans-25)
    green_2.off()
    print("Green light is off....")


"""
to find excution time
startTime=time.time()
ans=funtime()
endtime=time.time()
print("ex time",endtime-startTime)
"""

# while True:
#     red_2.on()
#     print("red - 2 in on....")
#     green_1.on()
#     print("green - 1 is on....")
#     sleep(5)
#     green_1.off()
#     print("green - 1 is off")
#     yellow_1.on()
#     print("yellow - 1 is on...")
#     ans = funtime()
#     sleep(1)
#     yellow_1.off()
#     print("yellow -1 is off...")
#     red_2.off()
#     print("red - 2 is off..")
#     red_1.on()
#     print("red - 1 is on..")