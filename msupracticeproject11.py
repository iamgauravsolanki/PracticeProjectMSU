# CSE 231 Spring 2014, Project 02  
# Section: [Your Section]  
# Date: [Submission Date]  
# Description: Calculates plants, soil, and fill material for an ornamental garden.  

import math  

def main():  
    # Prompt user for inputs  
    side_length = float(input("Enter garden side length (feet): "))  
    spacing = float(input("Enter plant spacing (inches): ")) / 12  # Convert to feet  
    bed_depth = float(input("Enter flowerbed depth (feet): "))  
    fill_depth = float(input("Enter fill depth (feet): "))  

    # Calculate areas  
    triangle_area = (side_length / 2) ** 2 / 2  # Area of one triangular flowerbed  
    circle_radius = side_length / 4  
    circle_area = math.pi * (circle_radius ** 2)  

    # Plant counts (truncated)  
    plants_triangle = int(triangle_area / (spacing ** 2))  
    plants_circle = int(circle_area / (spacing ** 2))  
    total_plants = 4 * plants_triangle + plants_circle  

    # Soil volume (cubic yards)  
    soil_triangle = (4 * triangle_area * bed_depth) / 27  # 1 yd³ = 27 ft³  
    soil_circle = (circle_area * bed_depth) / 27  
    total_soil = round(soil_triangle + soil_circle, 1)  

    # Fill volume (total garden volume - flowerbed volumes)  
    garden_volume = (side_length ** 2) * fill_depth / 27  
    fill_volume = round(garden_volume - (soil_triangle + soil_circle), 1)  

    # Output results  
    print("\n--- Garden Materials Report ---")  
    print(f"Plants: {plants_triangle} per triangle, {plants_circle} for circle")  
    print(f"Total Plants: {total_plants}")  
    print(f"Soil: {round(soil_triangle, 1)} yd³ (triangles), {round(soil_circle, 1)} yd³ (circle)")  
    print(f"Total Soil: {total_soil} yd³")  
    print(f"Fill Material: {fill_volume} yd³")  

if __name__ == "__main__":  
    main()  