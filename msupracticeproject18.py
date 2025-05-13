# CSE 231 Fall 2012, Project 02  
# Section: [Your Section]  
# Date: [Submission Date]  
# Description: Interactive Turtle graphics art generator with user-controlled parameters.  

import turtle  
import random  
import time  

def validate_input(prompt, min_val, max_val):  
    """Validate user input within a specified range."""  
    while True:  
        try:  
            value = int(input(prompt))  
            if min_val <= value <= max_val:  
                return value  
            print(f"Please enter a number between {min_val} and {max_val}.")  
        except ValueError:  
            print("Invalid input. Please enter a number.")  

def draw_shape(sides, size, color):  
    """Draw a regular polygon with given sides, size, and color."""  
    turtle.color(color)  
    turtle.begin_fill()  
    for _ in range(sides):  
        turtle.forward(size)  
        turtle.left(360 / sides)  
    turtle.end_fill()  

def main():  
    print("Geometric Art Generator")  
    print("----------------------")  
    print("Create concentric polygons with random colors!")  
    print("(Each shape will have 1 more side than the previous.)\n")  

    # Get user input  
    num_shapes = validate_input("Enter number of shapes (3-20): ", 3, 20)  
    base_size = validate_input("Enter base size (50-200 pixels): ", 50, 200)  

    # Setup turtle  
    turtle.speed(0)  
    turtle.bgcolor("black")  
    turtle.title("MSU CSE 231: Geometric Art")  

    # Draw shapes  
    for i in range(num_shapes):  
        # Random RGB color  
        r = random.random()  
        g = random.random()  
        b = random.random()  
        
        # Draw shape with increasing sides  
        draw_shape(i + 3, base_size - (i * 10), (r, g, b))  
        turtle.right(360 / num_shapes)  # Rotate for radial layout  

    # Finish  
    turtle.hideturtle()  
    print("\nArt complete! Close the window to exit.")  
    time.sleep(5)  # Pause to view  
    turtle.bye()  

if __name__ == "__main__":  
    main()  