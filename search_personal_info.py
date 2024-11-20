# Open file and let it read
with open("personal_info.txt", "r") as file:
    # Create a variable to read lines in the file
    lines = file.readlines()

    # Ask for a name input and remove extra spaces
    fullname = input("\nEnter the full name to search: ").strip()

# Find the respective name input in the file