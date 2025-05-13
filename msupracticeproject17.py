# CSE 231 Fall 2011, Project 02  
# Section: [Your Section]  
# Date: [Submission Date]  
# Description: Implements the 99 Trick mathematical game.  

def main():  
    print("The 99 Trick Game")  
    print("-----------------")  
    print("1. You pick a number (10-49) as the 'answer'.")  
    print("2. Your friend picks a number (50-99), and the magic begins!\n")  

    # Step 1: Get your answer (10-49)  
    while True:  
        try:  
            answer = int(input("Enter your number (10-49): "))  
            if 10 <= answer <= 49:  
                break  
            else:  
                print("Please enter a number between 10 and 49.")  
        except ValueError:  
            print("Invalid input. Please enter a number.")  

    factor = 99 - answer  

    # Step 2: Friend's number (50-99)  
    while True:  
        try:  
            friend_num = int(input("\nEnter your friend's number (50-99): "))  
            if 50 <= friend_num <= 99:  
                break  
            else:  
                print("Please enter a number between 50 and 99.")  
        except ValueError:  
            print("Invalid input. Please enter a number.")  

    # Calculations  
    sum_total = friend_num + factor  
    hundreds_digit = sum_total // 100  
    remaining = sum_total % 100  
    manipulated_num = remaining + hundreds_digit  
    result = friend_num - manipulated_num  

    # Output  
    print(f"\nFriend's number: {friend_num}")  
    print(f"After adding factor ({factor}): {sum_total}")  
    print(f"Manipulated number: {manipulated_num}")  
    print(f"Final result: {result} (matches your answer: {answer})")  

if __name__ == "__main__":  
    main()  