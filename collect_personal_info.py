# Open file and let the existing file append inputs and not override by using 'a'
with open("personal_info.txt", "a") as file:
    while True:
        # Ask for entries (name, age, address, contact no., email)
        full_name = input("Full Name: ")
        age = int(input("Age: "))
        contact = input("Contact Number: ")
        address = input("Address: ")
        email = input("Email: ")

        # Write the inputs to the file respectively
        file.write(f"Full Name: {full_name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Contact Number: {contact}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Email: {email}\n")

        # Ask for a new input
        another = input("\nDo you want to add another person? (yes/no): ").lower()
        if another == "yes":
            continue
        elif another == "no":
            print(f"\nData saved.")
            break