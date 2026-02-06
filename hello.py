sensor_data = [
    ("Sensor_A", "Field_1", "Temperature", "Celsius"),
    ("Sensor_B", "Field_2", "Humidity", "%"),
    ("Sensor_C", "Field_3", "Soil Moisture", "%"),
    ("Sensor_D", "Field_4", "Temperature", "Celsius"),
    ("Sensor_E", "Field_5", "Humidity", "%")
]
temp_count = 0
for sensor in sensor_data:
    if sensor[2]=="Temperature":
        temp_count+=1
print(f"No of Temperature sensors : {temp_count}")
for sensor in sensor_data:
    if "Humidity" in sensor:
        Humidity_i = sensor.index("Humidity")
        break
print(Humidity_i)
for index,sensor in enumerate(sensor_data):
    print(index,sensor)
for sensor in sensor_data:
    print(sensor)
for a,b,c,d in sensor_data:
    print(f"Sensor {a} in Field {b} measures {c} in unit {d}")