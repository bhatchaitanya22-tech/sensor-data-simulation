
import random

# simulate 10 sensor readings between 20 and 100
readings = [random.randint(20, 100) for _ in range(10)]
threshold = 70    # define safe threshold
alerts = []       # store readings exceeding threshold

# check each reading
for value in readings:
    if value > threshold:
        alerts.append(value)  # add to alert list

# display results
print("Sensor Readings:", readings)
if alerts:
    print("ALERT! Values exceeding threshold:", alerts)
else:
    print("All readings are within safe range.")

# compute basic statistics
print("Max Reading:", max(readings))
print("Min Reading:", min(readings))
print("Average Reading:", sum(readings)/len(readings))
