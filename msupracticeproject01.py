ROD_TO_METERS = 5.0292
METER_TO_FEET = 1 / 0.3048
METER_TO_MILES = 1 / 1609.34
RODS_PER_FURLONG = 40
WALKING_SPEED_MPH = 3.1
MINUTES_PER_HOUR = 60

rods = float(input("Input distance in rods: "))

meters = rods * ROD_TO_METERS
feet = meters * METER_TO_FEET
miles = meters * METER_TO_MILES
furlongs = rods / RODS_PER_FURLONG
time_minutes = (miles / WALKING_SPEED_MPH) * MINUTES_PER_HOUR

print(f"You entered {rods:.1f} rods.")
print(f"{meters:.3f} meters")
print(f"{feet:.3f} feet")
print(f"{miles:.6f} miles")
print(f"{furlongs:.3f} furlongs")
print(f"{time_minutes:.3f} minutes to walk")
