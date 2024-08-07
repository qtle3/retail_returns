#retail store return policy

def main():
    print("This program if you are eligible to return your item at the store.")
    receipt = input("Do you have your reciept: yes/no? ")
    if receipt == "no":
        print("You cannot return your item.")
    else:
        days = input("Has it been past 90 days: yes/no? ")
        if days == "yes":
            print("You cannot return your item.")
        else:
            food = input("is it a food item: yes/no: ")
            if food == "yes":
                print("You cannot return your item.")
            else:
                print("You can return your item!")
main()        
    
    
