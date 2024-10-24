# Author: Alejandro Simon (main + encoder)
# Partner: Owen Madden (decoder)
# Lab 6, Group 102

# Encoder function
def encode(password):
    # Initialize an empty string to store the encoded password
    encoded = ""
    # Loop through each digit in the password
    for digit in password:
        # Convert the digit to an integer, add 3, and take modulo 10 to wrap around if necessary
        encoded += str((int(digit) + 3) % 10)
    return encoded

# Decoder function
def decode(encoded_password):
    decoded = ""
    for i in range(len(encoded_password)):
        decoded += str((int(encoded_password[i]) - 3) % 10)
    return decoded

# Main function
def main():
    # Variable to store the encoded password
    encoded_password = ""
    # Infinite loop to keep displaying the menu until the user chooses to quit
    while True:
        # Display the menu options
        print("\nMenu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        # Prompt the user to enter an option
        option = input("\nPlease enter an option: ")

        # Option to encode a password
        if option == "1":
            password = input("Please enter your password to encode: ")
            # Check if the password is valid (8 digits and numeric)
            if len(password) == 8 and password.isdigit():
                # Encode the password and store it
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                # Inform the user if the password is invalid
                print("Invalid password. Please enter an 8-digit password containing only numbers.")
        # Option to decode a previously encoded password
        elif option == "2":
            # Check if there is an encoded password available
            if encoded_password:
                # Decode the encoded password and display both the encoded and original passwords
                original_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            else:
                # Inform the user if no password has been encoded yet
                print("No encoded password found. Please encode a password first.")
        # Option to quit the program
        elif option == "3":
            break
        # Handle invalid menu options
        else:
            print("Invalid option. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
