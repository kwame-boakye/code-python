# Dictionary to store character frequencies
char_count = {}

# Take user input and convert to lowercase for case-insensitivity
user_inp = input("Enter the string you want to check: ").lower()

# Step 1: Count occurrences of each character
for character in user_inp:
    char_count[character] = char_count.get(character, 0) + 1

# Step 2: Find the first non-repeating character
for character in user_inp:
    if char_count[character] == 1:
        print(f"The first non-repeating character is: {character}")
        break
else:
    print("No non-repeating character found.")
