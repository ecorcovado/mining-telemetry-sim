import time
import random

print("Starting Mining Telemetry Simulator...")
print("======================================")

while True:
    # Generate the simulated sensor data
    engine_temp = random.randint(50, 150)
    vibration = round(random.uniform(0.1, 5.0), 2)
    pressure = random.randint(1000, 2000)

    # Print the data to the screen
    print(f"Engine Temp: {engine_temp}C | Vibration: {vibration}g | Pressure: {pressure}kPa")

    # The Logic Trigger
    if engine_temp > 120:
        print("CRITICAL WARNING: SAFE TEMPERATURE EXCEEDED")

    # Pause for 2 seconds before looping again
    time.sleep(2)