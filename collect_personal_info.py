# Open file and let the existing file append inputs and not override by using 'a'
with open("personal_info.txt", "a") as file:
    # Loop for new inputs
    while True:
        # Ask for entries (name, age, address, contact no., email)
        print("\nEnter the following information:\n")

        full_name = input("Full Name: ")
        
        # Ask age until true/valid
        while True:
            try:
                age = int(input("Age: "))
                break
            except:
                print("Input is not an integer.") 

        # Ask contact no. until length is equal to 11 and are integers/digits
        while True:
            try:
                contact = input("Contact Number: ")
                if len(contact) != 11 or not contact.isdigit():
                    raise
                break
            except:
                print("Should be 11 digits.") 

        address = input("Address: ")

        # Ask email until it has a domain (contains '@' and '.')
        while True:
            try:
                email = input("Email: ")
                if '@' not in email or '.' not in email:
                    raise
                break
            except:
                print("Must be an email address. Make sure email domain is included ('@example.com').") 

        # Write the inputs to the file respectively
        file.write(f"Full Name: {full_name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Contact Number: {contact}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Email: {email}\n")
        file.write("-----\n") # Separator for new data

        # Ask for a new input
        another = input("\nDo you want to add another person? (yes/no): ").lower()
        if another == "yes":
            continue
        elif another == "no":
            print(f"\nData saved.")
            break
         # If input is neither 'yes' nor 'no', Loop until input is true/valid
        else:
            while True:
                try_again = input("Try again. (yes/no): ").lower()

                if try_again == "yes":
                    break
                elif try_again == "no":
                    print(f"\nData saved.")
                    exit()
                else:
                    print("Please input a valid answer.")