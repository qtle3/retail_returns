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


# Function to prompt the user for a yes/no response
def yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ["yes", "no"]:
            return response == "yes"
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


# Function to prompt the user for an integer value
def numeric_input(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter an number.")


# Function to log and print a message
def log_and_print(message):
    """Log the message and print it."""
    logging.info(message)
    print(message)


def main():
    print("This program if you are eligible to return your item at the store.")
    logging.info("Starting the return eligibility check.")

    # ask the user if they have a receipt
    if not yes_no_input("Do you have a receipt: yes/no? "):
        log_and_print("You cannot return your item.")
        return

    # ask the user if it has been past 90 days
    days = numeric_input("How many days has it been since the purchase? ")
    if days > return_policy["max_days"]:
        log_and_print("You cannot return your item.")
        return

    # ask the user if it is a food item
    if (
        yes_no_input("Is the item a food item: yes/no? ")
        and not return_policy["food_return"]
    ):
        log_and_print("Return denied: Food Items are not returnable.")
        return

    # ask the user if the item is in original condition
    if (
        not yes_no_input("Is the item in originl condition: yes/no? ")
        and return_policy["original_condition"]
    ):
        log_and_print("Return denied: Item is not in original condition.")
        return

    # Check if the item was a final sale
    if (
        yes_no_input("Was the item a final sale: yes/no? ")
        and not return_policy["final_sale"]
    ):
        log_and_print("Return denied: Item was a final sale.")
        return

    print("You can return your item!")


main()
