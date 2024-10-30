import random

list_numbers = 10

range_numbers = list(range(0, 10))
#Changing the order of the numbers to a random order
random.shuffle(range_numbers)

#Converting the list to a set to improve the time complexity of the code
range_numbers = set(range_numbers)

#Initialize 'missing_number' variable
missing_number = None

#Checking for the value that is not in the range
for num in range(1, 11):
    if num not in range_numbers:
        missing_number = num
        print(f"Missing number is {missing_number}")
        
