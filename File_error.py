filename = input("Enter the filename: ")

try:
    # Try to open and read the file
    with open(filename, "r") as infile:
        text = infile.read()

    # Modify text (uppercase for demo)
    modified = text.upper()

    # Save to new file
    new_filename = "updated_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified)

    print(f"Modified file saved as {new_filename}")

except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
