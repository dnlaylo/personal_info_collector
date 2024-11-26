try:
    # Open file and let it read
    with open("personal_info.txt", "r") as file:
        # Create a variable to read lines in the file
        lines = file.readlines()

    while True:
        # Ask for a name input and remove extra spaces
        fullname = input("\nEnter the full name to search: ").strip()
        # Initial value for 'found'
        found = False

        # Find the respective name input in the file
        for line in lines:
            if line.strip() == f"Full Name: {fullname}":
                # If name input matches data from file, then 'foun' becomes true
                found = True

            # found is set to True and prints lines until it reaches the separator line
            if found:
                if line.strip() == "-----": # Separator line
                    break
                print('\n', line.strip())

        if not found:
            print("\nInformation not found.")

        # Ask for another search
        another = input("\nDo you want to search for another name? (yes/no): ").strip().lower()
        if another == "yes":
            continue
        elif another == "no":
            print(f"\nExiting Program.")
            break
        else:
            while True:
                try_again = input("Try again. (yes/no): ").lower()

                if try_again == "yes":
                    break
                elif try_again == "no":
                    print(f"\nExiting Program.")
                    exit()
                else:
                    print("Please input a valid answer.")

except FileNotFoundError:
    print("File does not exist.")

# A reference code: https://python.plainenglish.io/what-is-linear-search-in-python-23bd2170f1a5