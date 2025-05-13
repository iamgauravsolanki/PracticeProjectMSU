# CSE 231 Fall 2008, Project 02
# Section: [Your Section]
# Date: [Submission Date]
# Description: Calculates and draws the angle between two user-defined lines using Turtle graphics.

import math
import turtle

def calculate_angle(x1, y1, x2, y2):
    """Calculate the acute angle (in degrees) between two lines."""
    # Calculate slopes
    try:
        m1 = y1 / x1 if x1 != 0 else float('inf')
    except ZeroDivisionError:
        m1 = float('inf')
    
    try:
        m2 = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float('inf')
    except ZeroDivisionError:
        m2 = float('inf')

    # Handle special cases
    if (m1 == float('inf') and m2 == 0) or (m2 == float('inf') and m1 == 0):
        return 90.0
    if m1 == float('inf') and m2 == float('inf'):
        return 0.0
    if m1 * m2 == -1:  # Perpendicular lines
        return 90.0

    # Calculate angle using arctangent
    try:
        angle_rad = math.atan(abs((m2 - m1) / (1 + m1 * m2)))
    except:
        return 90.0  # Handle division by zero cases
    
    angle_deg = math.degrees(angle_rad)
    return angle_deg if angle_deg <= 90 else 180 - angle_deg  # Ensure acute angle

def main():
    print("Turtle Graphics Angle Calculator")
    print("-------------------------------")
    print("Enter coordinates for two points to draw lines and calculate the angle between them.\n")

    # Prompt for coordinates
    try:
        x1 = float(input("Enter x-coordinate of Point 1: "))
        y1 = float(input("Enter y-coordinate of Point 1: "))
        x2 = float(input("Enter x-coordinate of Point 2: "))
        y2 = float(input("Enter y-coordinate of Point 2: "))
    except ValueError:
        print("Error: Please enter numeric values only.")
        return

    # Calculate angle
    angle = calculate_angle(x1, y1, x2, y2)
    print(f"\nAcute angle between lines: {angle:.2f}°")

    # Set up turtle graphics
    turtle.title("Angle Between Two Lines")
    turtle.speed(1)  # Slow speed for visibility
    
    # Draw first line (from origin to point 1)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(x1, y1)
    
    # Draw second line (from point 1 to point 2)
    turtle.goto(x2, y2)
    
    # Label the angle near the vertex
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.write(f" {angle:.2f}°", align="center", font=("Arial", 12, "bold"))
    
    turtle.done()

if __name__ == "__main__":
    main()