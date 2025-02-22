from time import sleep
from gpiozero import LED
import app
import time
# Define LEDs
red_1 = LED(2)
yellow_1 = LED(3)
green_1 = LED(4)

red_2 = LED(17)
yellow_2 = LED(27)
green_2 = LED(22)

red_3 = LED(10)
yellow_3 = LED(9)
green_3 = LED(8)

red_4 = LED(5)
yellow_4 = LED(6)
green_4 = LED(13)

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
    result=result.get_json()
    ans = result["number"]
    print("Green time :",ans)
    return ans

# while True:
#     red_1.on()
#     print("Red light is on....")
#     sleep(5)
#     red_1.off()
#     print("Red light is off....")
#     yellow_1.on()
#     print("yellow light is on....")
#     ans=funtime()
#     # sleep(3)
#     sleep(1)
#     yellow_1.off()
#     print("yellow light is off....")
#     # ans=time()
#     green_1.on()
#     print("Green light is on....")
#     sleep(ans-25)
#     green_1.off()
#     print("Green light is off....")

while True:
    
    red_1.on()
    red_2.on()
    red_3.on()
    yellow_4.on()
    ans = funtime()
    sleep(1)
    green_1.on()
    print("Green - 1 is on..")
    sleep(ans)
    green_1.off()
    print("Green - 1 is off...")
    yellow_1.on()
    print("Yellow - 1 is on..")
    ans=funtime() # 4 seconds execution time 
    sleep(1)
    red_1.on()
    red_2.off()
    green_2.on()
    print("Green - 2 is on.....")
    sleep(ans)

    green_2.off()
    print("Green - 2 is off...")
    yellow_2.on()
    print("Yellow - 2 is on..")
    ans=funtime() # 4 seconds execution time 
    sleep(1)
    red_2.on()
    red_3.off()
    green_3.on()
    print("Green - 3 is on.....")
    sleep(ans)

    green_3.off()
    print("Green - 3 is off...")
    yellow_3.on()
    print("Yellow - 3 is on..")
    ans=funtime() # 4 seconds execution time 
    sleep(1)
    red_3.on()
    red_4.off()
    green_4.on()
    print("Green - 4 is on.....")
    sleep(ans)
    green_4.off()
    print("Green - 4 is off...")








"""
to find excution time
startTime=time.time()
ans=funtime()
endtime=time.time()
print("ex time",endtime-startTime)
"""

