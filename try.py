from time import sleep
from gpiozero import LED
import app
import time
# Define LEDs
red = LED(4)
yellow = LED(6)
green = LED(2)

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
    red.on()
    print("Red light is on....")
    sleep(5)
    red.off()
    print("Red light is off....")
    yellow.on()
    print("yellow light is on....")
    ans=funtime()
    # sleep(3)
    sleep(1)
    yellow.off()
    print("yellow light is off....")
    # ans=time()
    green.on()
    print("Green light is on....")
    sleep(ans-25)
    green.off()
    print("Green light is off....")

"""
to find excution time
startTime=time.time()
ans=funtime()
endtime=time.time()
print("ex time",endtime-startTime)
"""