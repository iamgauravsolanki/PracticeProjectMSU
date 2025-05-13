# CSE 231 Spring 2013, Project 03  
# Section: [Your Section]  
# Date: [Submission Date]  
# Description: Vending machine change maker with optimal coin dispensation.  

def main():  
    # Initialize stock  
    stock = {'nickels': 25, 'dimes': 25, 'quarters': 25, 'ones': 0, 'fives': 0}  
    
    print("Welcome to the vending machine change maker program")  
    print("Change maker initialized.")  
    print("\nStock contains:")  
    print(f"{stock['nickels']} nickels")  
    print(f"{stock['dimes']} dimes")  
    print(f"{stock['quarters']} quarters")  
    print(f"{stock['ones']} ones")  
    print(f"{stock['fives']} fives")  

    while True:  
        # Get price input  
        price_input = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")  
        if price_input.lower() == 'q':  
            break  

        try:  
            price = float(price_input)  
            if price < 0 or round(price * 100) % 5 != 0:  
                print("Illegal price: Must be a non-negative multiple of 5 cents.")  
                continue  
        except ValueError:  
            print("Invalid input. Please enter a price or 'q' to quit.")  
            continue  

        price_cents = round(price * 100)  
        deposit_menu = """  
Menu for deposits:
'n' - deposit a nickel (5 cents)
'd' - deposit a dime (10 cents)
'q' - deposit a quarter (25 cents)
'o' - deposit a one dollar bill (100 cents)
'f' - deposit a five dollar bill (500 cents)
'c' - cancel the purchase
"""  
        print(deposit_menu)  

        paid_cents = 0  
        while paid_cents < price_cents:  
            dollars_owed = (price_cents - paid_cents) // 100  
            cents_owed = (price_cents - paid_cents) % 100  
            print(f"Payment due: {dollars_owed} dollars and {cents_owed} cents")  

            deposit = input("Indicate your deposit: ").lower()  
            if deposit == 'c':  
                break  
            elif deposit == 'n':  
                paid_cents += 5  
                stock['nickels'] += 1  
            elif deposit == 'd':  
                paid_cents += 10  
                stock['dimes'] += 1  
            elif deposit == 'q':  
                paid_cents += 25  
                stock['quarters'] += 1  
            elif deposit == 'o':  
                paid_cents += 100  
                stock['ones'] += 1  
            elif deposit == 'f':  
                paid_cents += 500  
                stock['fives'] += 1  
            else:  
                print(f"Illegal selection: {deposit}")  

        # Calculate change or refund  
        change_cents = paid_cents - price_cents if paid_cents >= price_cents else paid_cents  
        if change_cents > 0:  
            print("\nPlease take the change below.")  
            coins_dispensed = {'quarters': 0, 'dimes': 0, 'nickels': 0}  
            remaining_change = change_cents  

            # Greedy algorithm for change  
            for coin, value in [('quarters', 25), ('dimes', 10), ('nickels', 5)]:  
                if remaining_change >= value and stock[coin] > 0:  
                    max_coins = min(remaining_change // value, stock[coin])  
                    coins_dispensed[coin] = max_coins  
                    remaining_change -= max_coins * value  
                    stock[coin] -= max_coins  

            # Print dispensed coins  
            for coin, count in coins_dispensed.items():  
                if count > 0:  
                    print(f"{count} {coin}")  

            if remaining_change > 0:  
                print("\nMachine is out of change.")  
                print(f"See store manager for remaining refund.")  
                print(f"Amount due is: {remaining_change // 100} dollars and {remaining_change % 100} cents")  
        elif paid_cents == price_cents:  
            print("\nNo change due.")  

        # Print updated stock  
        print("\nStock contains:")  
        for coin, count in stock.items():  
            print(f"{count} {coin}")  

    # Final stock value  
    total_cents = (stock['nickels'] * 5 + stock['dimes'] * 10 + stock['quarters'] * 25 +
                   stock['ones'] * 100 + stock['fives'] * 500)  
    print(f"\nTotal: {total_cents // 100} dollars and {total_cents % 100} cents")  

if __name__ == "__main__":  
    main()  