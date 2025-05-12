# Function to calculate the Wind Chill Temperature (WCT) index
def calculate_wct(air_temp, air_speed):
    return 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16

# Part 1: Calculate and display the wind chill index for the given air temperature and wind speed pairs

# Predefined air temperature and wind speed pairs
data = [
    (10.0, 15),    # 10.0 degrees and 15 MPH
    (0.0, 25),     # 0.0 degrees and 25 MPH
    (-10.0, 35)    # -10.0 degrees and 35 MPH
]

# Loop through each pair and display the wind chill index
for air_temp, air_speed in data:
    wct_index = calculate_wct(air_temp, air_speed)
    print(f"Wind Chill Temperature Index for {air_temp}°F and {air_speed} MPH: {wct_index:.2f}")

# Part 2: Prompt user to enter their own air temperature and wind speed

# Get user input for air temperature and wind speed
user_air_temp = float(input("Enter the air temperature in Fahrenheit: "))
user_air_speed = float(input("Enter the wind speed in MPH: "))

# Calculate the wind chill index for user input
user_wct_index = calculate_wct(user_air_temp, user_air_speed)

# Display the result for the user's values
print(f"Wind Chill Temperature Index for {user_air_temp}°F and {user_air_speed} MPH: {user_wct_index:.2f}")
