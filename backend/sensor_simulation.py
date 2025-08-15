import random
import time

def generate_sensor_data():
    data = {
        "temperature": round(random.uniform(20, 80), 2),  # In °C
        "machine_speed": round(random.uniform(500, 1500), 2),  # RPM
        "energy_usage": round(random.uniform(100, 500), 2),  # kWh
    }
    return data

# Simulate real-time data
while True:
    sensor_data = generate_sensor_data()
    print(sensor_data)  # Prints new data every second
    time.sleep(1)
