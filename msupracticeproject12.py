# CSE 231 Fall 2012, Project 01  
# Section: [Your Section]  
# Date: [Submission Date]  
# Description: Calculates plants, soil, and fill for a semicircular/circular garden design.  

import math  

def main():  
    print("Calculate Garden Requirements")  
    print("-" * 30)  

    # User inputs  
    side = float(input("Enter length of side of garden (feet): "))  
    spacing = float(input("Enter spacing between plants (feet): "))  
    soil_depth = float(input("Enter depth of garden soil (feet): "))  
    fill_depth = float(input("Enter depth of fill (feet): "))  

    # Flowerbed radii  
    semicircle_radius = side / 4  
    circle_radius = side / 4  

    # Areas  
    semicircle_area = 0.5 * math.pi * (semicircle_radius ** 2)  
    circle_area = math.pi * (circle_radius ** 2)  

    # Plant counts (truncated)  
    plants_semicircle = int(semicircle_area / (spacing ** 2))  
    plants_circle = int(circle_area / (spacing ** 2))  
    total_plants = 4 * plants_semicircle + plants_circle  

    # Soil volumes (cubic yards)  
    soil_semicircle = (semicircle_area * soil_depth) / 27  # 1 yd³ = 27 ft³  
    soil_circle = (circle_area * soil_depth) / 27  
    total_soil = round(4 * soil_semicircle + soil_circle, 1)  

    # Fill volume (total garden volume - flowerbed volumes)  
    garden_volume = (side ** 2) * fill_depth / 27  
    fill_volume = round(garden_volume - (4 * soil_semicircle + soil_circle), 1)  

    # Results  
    print("\nRequirements")  
    print("-" * 30)  
    print(f"Plants for each semicircle garden: {plants_semicircle}")  
    print(f"Plants for the circle garden: {plants_circle}")  
    print(f"Total plants for garden: {total_plants}")  
    print(f"Soil for each semicircle garden: {round(soil_semicircle, 1)} cubic yards")  
    print(f"Soil for the circle garden: {round(soil_circle, 1)} cubic yards")  
    print(f"Total soil for garden: {total_soil} cubic yards")  
    print(f"Total fill for garden: {fill_volume} cubic yards")  

if __name__ == "__main__":  
    main()  