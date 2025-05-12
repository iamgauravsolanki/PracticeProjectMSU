# CSE 231 Spring 2013, Project 02  
# Section: [Your Section]  
# Date: [Submission Date]  
# Description: Verifies if a guessed six-digit number solves the equation: SLAYER + SLAYER + SLAYER = LAYERS.  

def main():  
    print("Guess a six-digit number SLAYER so that the following equation is true,")  
    print("where each letter stands for the digit in the position shown:")  
    print("SLAYER + SLAYER + SLAYER = LAYERS\n")  

    # Prompt for guess  
    guess = int(input("Enter your guess for SLAYER: "))  

    # Check if guess is 6 digits  
    if guess < 100000 or guess > 999999:  
        print("\nYour guess is incorrect:")  
        print("SLAYER must be a 6-digit number.")  
    else:  
        # Extract digits (S, L, A, Y, E, R)  
        S = guess // 100000  
        L = (guess // 10000) % 10  
        A = (guess // 1000) % 10  
        Y = (guess // 100) % 10  
        E = (guess // 10) % 10  
        R = guess % 10  

        # Reconstruct LAYERS (shift left by 1 digit + S at the end)  
        slayer_sum = guess * 3  
        layers = L * 100000 + A * 10000 + Y * 1000 + E * 100 + R * 10 + S  

        # Check if equation holds  
        if slayer_sum == layers:  
            print("\nYour guess is correct:")  
            print(f"SLAYER + SLAYER + SLAYER = {slayer_sum}")  
            print(f"LAYERS = {layers}")  
        else:  
            print("\nYour guess is incorrect:")  
            print(f"SLAYER + SLAYER + SLAYER = {slayer_sum}")  
            print(f"LAYERS = {layers}")  

    print("Thanks for playing.")  

if __name__ == "__main__":  
    main()  