# Open file and let it read
with open("personal_info.txt", "r") as file:
    # Create a variable to read lines in the file
    lines = file.readlines()

while True:
    # Ask for a name input and remove extra spaces
    fullname = input("\nEnter the full name to search: ").strip()

# Find the respective name input in the file
    for line in lines:
        if line.strip() == f"Full Name: {fullname}":
            if line.strip() == "-----":
                break
            print('\n', line.strip())
