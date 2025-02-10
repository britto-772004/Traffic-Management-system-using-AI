from flask import Flask, request, jsonify
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

# Define GPIO Pins for LEDs
lanes = [
    {"red": 4, "yellow": 3, "green": 2},
    {"red": 7, "yellow": 6, "green": 5},
    {"red": 10, "yellow": 9, "green": 8},
    {"red": 13, "yellow": 12, "green": 11}
]

# Setup GPIO
GPIO.setmode(GPIO.BCM)
for lane in lanes:
    for light in lane.values():
        GPIO.setup(light, GPIO.OUT)
        GPIO.output(light, 0)  # Turn OFF initially

# Function to control LEDs
def set_traffic_lights(active_lane, green_time=5):
    for i, lane in enumerate(lanes):
        GPIO.output(lane["red"], 1 if i != active_lane else 0)
        GPIO.output(lane["yellow"], 0)
        GPIO.output(lane["green"], 1 if i == active_lane else 0)
    
    time.sleep(green_time)  # Green ON
    
    # Switch to Yellow before turning Red
    GPIO.output(lanes[active_lane]["green"], 0)
    GPIO.output(lanes[active_lane]["yellow"], 1)
    time.sleep(2)
    
    GPIO.output(lanes[active_lane]["yellow"], 0)  # Yellow OFF

# API to trigger lights
@app.route("/update-lights", methods=["POST"])
def update_lights():
    for i in range(len(lanes)):  
        set_traffic_lights(i, 5)  # Green for 5 sec each lane

    return jsonify({"message": "Traffic light cycle completed"})

# API to turn on a specific lane manually
@app.route("/set-lane/<int:lane_id>", methods=["POST"])
def set_lane(lane_id):
    if lane_id < 0 or lane_id >= len(lanes):
        return jsonify({"error": "Invalid lane ID"}), 400
    
    set_traffic_lights(lane_id, 10)  # Default 10s green
    return jsonify({"message": f"Lane {lane_id+1} is now Green"})

# Cleanup GPIO on exit
@app.route("/shutdown", methods=["POST"])
def shutdown():
    GPIO.cleanup()
    return jsonify({"message": "GPIO cleaned up and server shutting down"}), 200

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()
