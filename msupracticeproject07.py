# proj01.py
# Section: CSE 231 - Fall 2009
# Project #1
# Date: [Insert today's date]
# Author: [Your Name]
# Description: Predict US population based on user-input future years

# Constants
STARTING_POPULATION = 307357870  # Fixed base population
SECONDS_PER_YEAR = 365 * 24 * 60 * 60  # 365 days, 24 hours, 60 minutes, 60 seconds

BIRTH_RATE = 7         # one birth every 7 seconds
DEATH_RATE = 13        # one death every 13 seconds
IMMIGRATION_RATE = 35  # one immigrant every 35 seconds

# Prompt for user input
num_years_str = input("Enter number of years into the future: ")
num_years = int(num_years_str)

# Time calculations
total_seconds = num_years * SECONDS_PER_YEAR

# Population change calculations
num_births = total_seconds // BIRTH_RATE
num_deaths = total_seconds // DEATH_RATE
num_immigrants = total_seconds // IMMIGRATION_RATE

# New predicted population
predicted_population = STARTING_POPULATION + num_births - num_deaths + num_immigrants

# Output result
print ("Predicted population in", num_years, "years is", int(predicted_population))
