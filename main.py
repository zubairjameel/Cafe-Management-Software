def display_menu(menu):
    print("\nMenu:")
    for item_num, (item, price) in menu.items():
        print(f"{item_num}. {item}: £{price:.2f}")

def main():
    greetings = input("Welcome to the Restaurant \nDo you want to order? (yes/no): ").strip().lower()

    if greetings == "yes":
        print("Okay, Let's get started")

        menu = {
            1: ("Burger", 3.00),
            2: ("Pizza", 2.00),
            3: ("Fries", 1.50),
            4: ("Sandwich", 2.50),
            5: ("Salad", 1.00),
            6: ("Pasta", 3.50),
            7: ("Sushi", 5.00),
            8: ("Steak", 7.00),
            9: ("Chicken", 4.00),
            10: ("Rice", 2.50),
            11: ("Noodles", 3.00)
        }

        ordered_items = []

        while True:
            display_menu(menu)

            order = input("What would you like to order? (Enter item number, or 'done' to finish): ").strip().lower()

            if order == "done":
                break
            elif order.isdigit() and int(order) in menu:
                ordered_items.append(menu[int(order)][0])
                print(f"Added {menu[int(order)][0]} to your order.")
            else:
                print("Invalid input. Please enter a valid item number.")

        card_number = input("Please add your card in the machine (enter card number): ").strip()
        if card_number.isdigit():
            print("Thank you")
            print("\nYou have ordered:")
            for item in ordered_items:
                print("- " + item)
        else:
            print("Invalid card number. Please try again.")

    elif greetings == "no":
        print("Have A Nice Day!")
    else:
        print("Good Bye")

if __name__ == "__main__":
    main()
