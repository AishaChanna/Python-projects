menu = {
    'appetizers': {
        'bruschetta': 150,
        'calamari': 200,
        'stuffed mushrooms': 180,
        'samosa': 50,
        'pakora': 40,
    },
    'main courses': {
        'grilled salmon': 500,
        'steak': 700,
        'chicken parmesan': 450,
        'biryani': 350,
        'karahi': 400,
        'nihari': 380,
    },
    'desserts': {
        'cheesecake': 250,
        'tiramisu': 300,
        'lava cake': 280,
        'gulab jamun': 100,
        'jalebi': 120,
    },
    'beverages': {
        'coffee': 70,
        'tea': 60,
        'wine': 400,
        'lassi': 80,
        'rooh afza': 50,
    }
}

customer_reviews = []


def display_menu():
    print("\nWelcome to OrderPal Restaurant")
    print("Menu:")
    for category, items in menu.items():
        print(f"\n{category.capitalize()}:")
        for item, price in items.items():
            print(f"  {item.capitalize()}: Rs.{price}")


def display_options():
    print("\nOptions:")
    print("1. Add item to order")
    print("2. View current order total")
    print("3. Remove item from order")
    print("4. Clear order")
    print("5. Finalize order")
    print("6. Reserve a table")
    print("7. Leave a review")
    print("8. View reviews")
    print("9. Exit")


def display_order(order_items, order_total, special_requests):
    if order_items:
        print("\nYour current order:")
        for item, details in order_items.items():
            print(
                f"{item.capitalize()} x{details['quantity']}: Rs.{menu[details['category']][item] * details['quantity']}"
            )
        print(f"Current order total: Rs.{order_total}")
        if special_requests:
            print(f"Special requests: {special_requests}")
    else:
        print("Your order is empty.")


def display_reviews():
    if customer_reviews:
        print("\nCustomer Reviews:")
        for review in customer_reviews:
            print(f"Name: {review['name']}")
            print(f"Review: {review['review']}\n")
    else:
        print("No reviews yet.")


def take_order():
    order_items = {}
    order_total = 0
    special_requests = ""
    customer_details = {}

    display_menu()
    display_options()

    while True:
        choice = input("\nChoose an option: ").strip()

        if choice == '1':
            category = input(
                "Enter the category of the item you want to order (appetizers, main courses, desserts, beverages): "
            ).strip().lower()
            if category in menu:
                item = input(
                    f"Enter the name of the item you want to order from {category}: "
                ).strip().lower()
                if item in menu[category]:
                    quantity = int(
                        input(
                            f"How many {item.capitalize()}s would you like to add? "
                        ))
                    if item in order_items:
                        order_items[item]['quantity'] += quantity
                    else:
                        order_items[item] = {
                            'quantity': quantity,
                            'category': category
                        }
                    order_total += menu[category][item] * quantity
                    print(
                        f"{item.capitalize()} x{quantity} has been added to your order."
                    )
                else:
                    print(
                        f"{item.capitalize()} is not in the {category} menu.")
            else:
                print(f"{category.capitalize()} is not a valid category.")

        elif choice == '2':
            display_order(order_items, order_total, special_requests)

        elif choice == '3':
            item = input("Enter the name of the item you want to remove: "
                         ).strip().lower()
            if item in order_items:
                quantity = int(
                    input(
                        f"How many {item.capitalize()}s would you like to remove? "
                    ))
                if quantity >= order_items[item]['quantity']:
                    order_total -= menu[order_items[item]['category']][
                        item] * order_items[item]['quantity']
                    del order_items[item]
                    print(
                        f"All {item.capitalize()}s have been removed from your order."
                    )
                else:
                    order_items[item]['quantity'] -= quantity
                    order_total -= menu[order_items[item]
                                        ['category']][item] * quantity
                    print(
                        f"{item.capitalize()} x{quantity} has been removed from your order."
                    )
            else:
                print(f"{item.capitalize()} is not in your order.")

        elif choice == '4':
            order_items.clear()
            order_total = 0
            special_requests = ""
            print("Your order has been cleared.")

        elif choice == '5':
            special_requests = input(
                "Any special requests for your order? ").strip()
            display_order(order_items, order_total, special_requests)
            print(f"The total amount of your order is Rs.{order_total}")
            customer_details['name'] = input(
                "Please enter your name: ").strip()
            customer_details['phone'] = input(
                "Please enter your phone number: ").strip()
            print(
                f"Thank you for your order, {customer_details['name']}! Have a great day!"
            )
            break

        elif choice == '6':
            customer_details['name'] = input(
                "Please enter your name: ").strip()
            customer_details['phone'] = input(
                "Please enter your phone number: ").strip()
            customer_details['table_time'] = input(
                "Please enter your preferred reservation time: ").strip()
            print(
                f"Thank you, {customer_details['name']}! Your table has been reserved for {customer_details['table_time']}."
            )

        elif choice == '7':
            review = {}
            review['name'] = input("Please enter your name: ").strip()
            review['review'] = input("Please leave your review: ").strip()
            customer_reviews.append(review)
            print("Thank you for your review!")

        elif choice == '8':
            display_reviews()

        elif choice == '9':
            print("Exiting the system. Thank you!")
            break

        else:
            print("Invalid option, please try again.")


take_order()
