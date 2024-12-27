def store_hours():
    print("Store hours are from 9 AM - 7 PM")

def products_available():
    products = [
        'Starbucks Coffee Mug',
        'Buccee\'s red t-shirt',
        'Buccee\'s blanket',
        'Burger King Crown',
        'Jurassic World T-rex toy'
    ]
    for product in products:
        print(product)

def product_prices():
    prices = {
        'Starbucks Coffee Mug': 4.50,
        'Buccee\'s red t-shirt': 10.00,
        'Buccee\'s blanket': 11.00,
        'Burger King Crown': 5.50,
        'Jurassic World T-rex toy': 12.00
    }
    for product, price in prices.items():
        print(f"{product}: ${price}")

def display_menu():
    print("1. See store hours")
    print("2. See products available")
    print("3. See product prices")
    print("4. Exit conversation")

def main():
    print("Hello and welcome to our store, what's your name?")
    name = input("My name is: ")
    print(f"Hey {name}, welcome in, it's really nice to meet you!")
    
    print("How old are you?")
    age = int(input("My age is: "))
    
    if 1 <= age <= 25:
        print("Wow, you're really young!")
    elif 26 <= age <= 50:
        print("Wow, that's a good age!")
    elif 51 <= age <= 80:
        print("Oh wow! That's a very wise age")
    elif age > 80:
        print("You must have a wealth of wisdom and life experience by now.")
    
    print("How may I help you?")
    
    program_loop = True
    
    while program_loop:
        display_menu()
        user_choice = int(input("Please enter your choice (1-4): "))
        
        if user_choice == 1:
            store_hours()
        elif user_choice == 2:
            products_available()
        elif user_choice == 3:
            product_prices()
        elif user_choice == 4:
            print("Thank you for visiting!")
            program_loop = False  # Stops the loop and ends the program
        else:
            print("\nSorry, not a valid choice. Please try again!")

if __name__ == "__main__":
    main()