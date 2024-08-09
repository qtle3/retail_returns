# retail store return policy

return_policy = {}


def main():
    print("This program if you are eligible to return your item at the store.")
    # ask the user if they have a receipt
    receipt = input("Do you have your reciept: yes/no? ")

    # if the user does not have a receipt, they cannot return the item
    if receipt == "no":
        print("You cannot return your item.")
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
