# This script greets the user and calculates a "lucky number"

# We define 'user_name' by asking the user for their name.
user_name = input("Hello! What's your name? ")

# This variable 'favorite_number' is now active (uncommented).
favorite_number = 7

# We greet the user using an f-string to easily include their name.
print(f"Nice to meet you, {user_name}!")

# Now we can calculate 'lucky_number' because 'favorite_number' is defined.
lucky_number = favorite_number * 2

# We print the calculated lucky number.
print(f"Your lucky number is: {lucky_number}")

# A final friendly message.
print("Have a great day!")