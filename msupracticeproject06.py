# proj01.py
# Section: BCA 2A
# Date: 2025-05-12
# Project 6 - Miles per Hour Conversions

# Constants
MILES_TO_METERS = 1609.34
SECONDS_PER_HOUR = 3600
BARLEYCORNS_PER_METER = 117.647
YARDS_PER_FURLONG = 220
FEET_PER_MILE = 5280
SECONDS_PER_FORTNIGHT = 14 * 24 * 3600
SPEED_OF_SOUND = 1130  # feet per second
SPEED_OF_LIGHT = 299_792_458  # meters per second

# Input
mph = float(input("Enter speed in miles per hour: "))

# Conversions
meters_per_hour = mph * MILES_TO_METERS
barleycorns_per_hour = meters_per_hour * BARLEYCORNS_PER_METER
barleycorns_per_day = barleycorns_per_hour * 24

feet_per_sec = mph * FEET_PER_MILE / SECONDS_PER_HOUR
mach = feet_per_sec / SPEED_OF_SOUND

meters_per_sec = meters_per_hour / SECONDS_PER_HOUR
percentage_speed_of_light = (meters_per_sec / SPEED_OF_LIGHT) * 100

furlongs = mph * 1760 / YARDS_PER_FURLONG  # 1 mile = 1760 yards
furlongs_per_fortnight = furlongs * 24 * 14  # 14 days of 24 hours

# Output
print("\nConverted Values:")
print("Barleycorns per day: ", round(barleycorns_per_day, 2))
print("Furlongs per fortnight: ", round(furlongs_per_fortnight, 2))
print("Mach number: ", round(mach, 4))
print("Percentage of the speed of light: ", round(percentage_speed_of_light, 10))
