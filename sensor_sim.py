import random

readings = [random.randint(20, 100) for _ in range(10)]
threshold = 70

print("Sensor Readings:", readings)

alerts = []

for value in readings:
    if value > threshold:
        alerts.append(value)

if alerts:
    print("ALERT! Values exceeding threshold:", alerts)
else:
    print("All readings within safe range.")

print("Statistics")
print("Max:", max(readings))
print("Min:", min(readings))
print("Average:", sum(readings) / len(readings))
