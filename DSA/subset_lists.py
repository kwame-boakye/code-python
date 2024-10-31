list_1 = list(range(0, 11))
list_2 = list(range(0, 0))

print(f"Mother set: ", list_1 , "\nOther list: ", list_2, '\n')

def check_for_subset(set_1, set_2):
    count = 0
    for num in list_2:
        if num in list_1:
            count += 1
    if count == len(list_2) or len(list_2) == 0:
        print(f"The second list is a subset of the first list")
    else:
        print(f"The second list is not a subset of the first list")


check_for_subset(list_1, list_2)

#use the randint() to improve upon this code
