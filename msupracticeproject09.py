# CSE 231 Fall 2011, Project 01  
# Section: [Your Section]  
# Date: [Submission Date]  
# Description: Visualizes U.S. national debt by calculating stack height in miles and lunar distance equivalents.  

def main():  
    # Constants  
    BILL_THICKNESS_INCHES = 0.0043  
    INCHES_TO_MILES = 1 / 63360  # 1 mile = 63,360 inches  
    MOON_DISTANCE_MILES = 238857  

    # Prompt user for debt and bill denomination  
    debt_str = input("Enter U.S. national debt in dollars (e.g., 31900000000000): ")  
    denomination_str = input("Enter bill denomination (e.g., 1, 100, 100000): ")  

    # Convert to floats  
    debt = float(debt_str)  
    denomination = float(denomination_str)  

    # Calculate total bills and stack height in miles  
    total_bills = debt / denomination  
    height_inches = total_bills * BILL_THICKNESS_INCHES  
    height_miles = height_inches * INCHES_TO_MILES  

    # Calculate lunar distance multiples  
    moon_multiples = height_miles / MOON_DISTANCE_MILES  

    # Results  
    print("\nVisualizing U.S. National Debt:")  
    print(f"Debt: ${debt:,.2f} in ${denomination:,.0f} bills")  
    print(f"Stack Height: {height_miles:,.2f} miles")  
    print(f"Moon Distance Multiples: {moon_multiples:,.2f}x (avg. moon distance = 238,857 miles)")  

if __name__ == "__main__":  
    main()  