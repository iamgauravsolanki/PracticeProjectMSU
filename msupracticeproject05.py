# ------------------------------------------------------------
# CSE 231 - Fall 2008
# Project #1
# Name: Your Name Here
# Section: Your Section
# Date: Today's Date
# Description: This program takes gallons of gasoline as input,
# then calculates and displays various related information.
# ------------------------------------------------------------

# Constants
LITERS_PER_GALLON = 3.7854
GALLONS_PER_BARREL = 19.5
CO2_PER_GALLON = 20.0  # in pounds
BTU_PER_GALLON_GAS = 115000.0
BTU_PER_GALLON_ETHANOL = 75700.0
PRICE_PER_GALLON = 4.00

# Input
gallonsStr = input("Please enter the number of gallons of gasoline: ")
gallons = float(gallonsStr)

# Calculations
liters = gallons * LITERS_PER_GALLON
barrels = gallons / GALLONS_PER_BARREL
co2_produced = gallons * CO2_PER_GALLON
ethanol_equiv = (gallons * BTU_PER_GALLON_GAS) / BTU_PER_GALLON_ETHANOL
total_cost = gallons * PRICE_PER_GALLON

# Output
print
print ("Gallons entered:", gallons)
print ("Liters:", liters)
print ("Barrels of oil required:", barrels)
print ("Pounds of CO2 produced:", co2_produced)
print ("Equivalent energy amount in ethanol gallons:", ethanol_equiv)
print ("Cost in US dollars: $", total_cost)
