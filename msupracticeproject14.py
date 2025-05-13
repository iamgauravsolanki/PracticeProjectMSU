# CSE 231 Spring 2010, Project 02  
# Section: [Your Section]  
# Date: [Submission Date]  
# Description: Implements General MacArthur's number trick to reveal birth month and age.  

def main():  
    print("General MacArthur's Number Trick")  
    print("-------------------------------")  
    print("Enter your birth month (1-12) and age to reveal the magic!")  

    # Prompt for inputs  
    month = int(input("Enter your birth month (e.g., 2 for February): "))  
    age = int(input("Enter your age: "))  

    # Calculate the "special number"  
    special_number = (month * 2 + 5) * 50 + age - 365  
    result = special_number + 115  

    # Extract month and age from result  
    calculated_month = result // 100 if result >= 1000 else result // 100  
    calculated_age = result % 100  

    # Output results  
    print(f"\nSpecial number: {special_number}")  
    print(f"After adding 115: {result}")  
    print(f"Magic reveal: You were born in month {calculated_month} and are {calculated_age} years old!")  

if __name__ == "__main__":  
    main()  