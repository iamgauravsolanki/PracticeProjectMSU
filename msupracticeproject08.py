# CSE 231 Spring 2010, Project 01  
# Section: [Your Section]  
# Date: [Submission Date]  
# Description: Calculates relativistic time dilation and mass increase for a spaceship near light speed.  

def main():  
    # Constants  
    c = 299792458  # Speed of light (m/s)  
    ship_mass_rest = 70000  # Ship mass at rest (kg)  
    destinations = {  
        "Alpha Centauri": 4.3,  
        "Barnard's Star": 6.0,  
        "Betelgeuse": 309,  
        "Andromeda Galaxy": 2000000  
    }  

    # Prompt user for velocity (% of light speed)  
    percent_c = float(input("Enter percentage of light speed (e.g., 50 for 50%): "))  
    v = (percent_c / 100) * c  # Convert to m/s  

    # Calculate relativistic factor  
    factor = 1 / ((1 - (v**2 / c**2)) ** 0.5)  

    # Results  
    print("\nRelativistic Effects at {:.1f}% Light Speed:".format(percent_c))  
    print("Ship Mass (at rest): {:,} kg".format(ship_mass_rest))  
    print("Ship Mass (at speed): {:.2f} kg (x{:.6f})".format(ship_mass_rest * factor, factor))  

    print("\nTime Experienced by Astronauts:")  
    for name, ly in destinations.items():  
        earth_time = ly  # Earth time (years)  
        astronaut_time = earth_time / factor  # Astronaut time (years)  
        print(f"{name}: {astronaut_time:.6f} years (vs {earth_time} Earth years)")  

if __name__ == "__main__":  
    main()  