# retail store return policy

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


# Policy for returning items at a retail store
return_policy = {
    "max_days": 90,
    "food_return": False,
    "final_sale": False,
    "original_condition": True,
}


def yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ["yes", "no"]:
            return response
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def log_and_print(message):
    """Log the message and print it."""
    logging.info(message)
    print(message)


def main():
    print("This program if you are eligible to return your item at the store.")
    logging.info("return denied: customer does not have a receipt")

    # ask the user if they have a receipt
    if not yes_no_input("Do you have a receipt: yes/no? "):
        log_and_print("You cannot return your item.")
        return

    # ask the user if it has been past 90 days
    days = input("Has it been past 90 days: yes/no? ")
    if days == "yes":
        print("You cannot return your item.")
        return

    # ask the user if it is a food item
    food = input("is it a food item: yes/no: ")
    if food == "yes":
        print("You cannot return your item.")
        return

    # Check if the item was a final sale
    final_sale = input("Was the item marked as 'Final Sale': yes/no? ").strip().lower()
    if final_sale == "yes":
        print("You cannot return your item.")
        return

    # Check the condition of the item
    condition = (
        input("Is the item in original, unused condition: yes/no? ").strip().lower()
    )
    if condition == "no":
        print("You cannot return your item.")
        return

    print("You can return your item!")


main()
