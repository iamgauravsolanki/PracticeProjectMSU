# CSE 231 Spring 2008, Project 02  
# Section: [Your Section]  
# Date: [Submission Date]  
# Description: Implements Einstein's 1089 number puzzle.  

def main():  
    print("Einstein's Number Puzzle")  
    print("------------------------")  
    print("Enter a 3-digit number where the first and last digits differ by at least 2.")  

    # Prompt for input  
    num = int(input("Your number: "))  

    # Extract digits  
    hundreds = num // 100  
    tens = (num // 10) % 10  
    ones = num % 10  

    # Reverse the number  
    reversed_num = ones * 100 + tens * 10 + hundreds  

    # Calculate positive difference  
    difference = abs(num - reversed_num)  

    # Reverse the difference  
    diff_hundreds = difference // 100  
    diff_tens = (difference // 10) % 10  
    diff_ones = difference % 10  
    reversed_diff = diff_ones * 100 + diff_tens * 10 + diff_hundreds  

    # Sum to get 1089  
    result = difference + reversed_diff  

    # Output steps  
    print(f"\nYour number: {num}")  
    print(f"Reversed number: {reversed_num}")  
    print(f"Difference: {difference}")  
    print(f"Reversed difference: {reversed_diff}")  
    print(f"Final result: {result} (always 1089!)")  

if __name__ == "__main__":  
    main()  